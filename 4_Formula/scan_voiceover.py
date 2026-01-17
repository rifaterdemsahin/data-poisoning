import os
import json
import glob

ROOT_DIR = r"F:\aisecuritycourse"
OUTPUT_FILE = r"F:\aisecuritycourse\data-poisoning\4_Formula\voice_over_script.md"
THIS_PROJECT = "data-poisoning"

TEMPLATE_PROJECT_STRUCTURE = """
## 📂 Project Structure: {project_name} (0:00 - 0:30)

**Visual**: 🗂️ Highlighting each folder in the project view.
**Voice**:
"We start by scanning the project structure for {project_name}:"

{structure_list}
"""

TEMPLATE_NOTEBOOK_INTRO = """
## 🎬 Introduction to Notebook (0:30 - 1:00)

**Visual**: 🖼️ Title Slide / Top of Notebook `[[{notebook_path}]]`
**Voice**:
"We're exploring the notebook for {project_name}. This notebook demonstrates..."
"""

TEMPLATE_STEP = """
## 🛠️ {step_title}

**Visual**: 📜 Scrolling to '{step_title}' `[[{notebook_path}#L{line_number}]]`.
**Voice**:
"In this step..."
"""

def get_project_structure_list(project_path):
    structure = []
    # Standard 7-folder structure
    standard_folders = [
        "1_Real", "2_Environment", "3_UI", "4_Formula", 
        "5_Symbols", "6_Semblance", "7_Testing"
    ]
    
    found_standard = False
    for folder in standard_folders:
        full_path = os.path.join(project_path, folder)
        if os.path.isdir(full_path):
            found_standard = True
            try:
                readme = f"[[{folder}/README.md]]" if os.path.exists(os.path.join(full_path, "README.md")) else "No README"
            except:
                readme = "No README"
            structure.append(f"- **{folder}**: `{readme}`")
    
    if not found_standard:
        # Fallback to listing top-level dirs/files
        for item in os.listdir(project_path):
            if item.startswith('.'): continue
            item_path = os.path.join(project_path, item)
            relative_path = item # relative to project root
            if os.path.isdir(item_path):
                 structure.append(f"- **{item}/**")
            elif item.endswith('.md') or item.endswith('.ipynb'):
                 structure.append(f"- **{item}**: `[[{item}]]`")
                 
    return "\n".join(structure)

def find_main_notebook(project_path):
    # Try 5_Symbols first
    symbols_path = os.path.join(project_path, "5_Symbols")
    if os.path.isdir(symbols_path):
        notebooks = glob.glob(os.path.join(symbols_path, "*.ipynb"))
        if notebooks:
            return max(notebooks, key=os.path.getsize) # return largest
            
    # Try recursive search if not found
    notebooks = glob.glob(os.path.join(project_path, "**", "*.ipynb"), recursive=True)
    if notebooks:
         return max(notebooks, key=os.path.getsize)
         
    return None

def parse_notebook_steps(notebook_path, project_rel_path):
    steps = []
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
            
        cells = nb.get('cells', [])
        line_count = 1
        
        for cell in cells:
            source = cell.get('source', [])
            cell_type = cell.get('cell_type', '')
            
            # Simple header extraction
            if cell_type == 'markdown':
                content = "".join(source).strip()
                if content.startswith('#'):
                    # It's a header
                    header = content.split('\n')[0].strip('# ').strip()
                    steps.append({
                        'title': header,
                        'line': line_count # Approximation
                    })
            
            # basic line count update (source lines + metadata overhead)
            line_count += len(source) + 5 

    except Exception as e:
        print(f"Error reading notebook {notebook_path}: {e}")
        
    return steps

def generate_script_for_project(project_name, project_path):
    output = []
    output.append(f"\n# 🚀 Project: {project_name}\n")
    
    # Structure
    structure_list = get_project_structure_list(project_path)
    output.append(TEMPLATE_PROJECT_STRUCTURE.format(project_name=project_name, structure_list=structure_list))
    
    # Notebook
    notebook_path = find_main_notebook(project_path)
    if notebook_path:
        rel_notebook_path = os.path.relpath(notebook_path, start=ROOT_DIR).replace('\\', '/')
        output.append(TEMPLATE_NOTEBOOK_INTRO.format(project_name=project_name, notebook_path=rel_notebook_path))
        
        steps = parse_notebook_steps(notebook_path, rel_notebook_path)
        for i, step in enumerate(steps):
             link_path = os.path.relpath(notebook_path, ROOT_DIR).replace('\\', '/')
             
             output.append(TEMPLATE_STEP.format(
                 step_title=f"Step {i+1}: {step['title']}",
                 notebook_path=link_path,
                 line_number=step['line']
             ))
    else:
        output.append("\n**Note**: No notebook found for this project.\n")
        
    return "\n".join(output)

def main():
    projects = [d for d in os.listdir(ROOT_DIR) if os.path.isdir(os.path.join(ROOT_DIR, d))]
    
    # Sort to keep order
    projects.sort()
    
    new_content = []
    
    for project in projects:
        if project == THIS_PROJECT:
            continue
            
        print(f"Scanning {project}...")
        project_path = os.path.join(ROOT_DIR, project)
        
        # Check if "real" project (has readme or notebook)
        has_readme = os.path.exists(os.path.join(project_path, "README.md"))
        has_notebook = find_main_notebook(project_path) is not None
        
        if has_readme or has_notebook:
            script_section = generate_script_for_project(project, project_path)
            new_content.append(script_section)
    
    if new_content:
        # Append to file
        with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
            f.write("\n\n" + "-"*50 + "\n\n")
            f.write("\n\n".join(new_content))
        print("Done! Updated voice_over_script.md")
    else:
        print("No new content found to add.")

if __name__ == "__main__":
    main()
