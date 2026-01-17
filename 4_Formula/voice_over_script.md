# 🎙️ Voice-Over Script: Backdoor Attack Demo

## 📂 Project Structure (0:00 - 0:30)

**Visual**: 🗂️ Highlighting each folder in the project view.
**Voice**:
"We start by scanning the project structure, organized into seven key stages:"

1. "**1_Real**: `[[1_Real/README.md]]` Contains the foundational reality and raw data."
2. "**2_Environment**: `[[2_Environment/README.md]]` Sets up the execution environment."
3. "**3_UI**: `[[3_UI/README.md]]` Handles the user interface components."
4. "**4_Formula**: `[[4_Formula/README.md]]` Holds our methodology and scripts, including this one."
5. "**5_Symbols**: `[[5_Symbols/backdoor_attack_demo.ipynb]]` Contains the core logic and our demonstration notebook."
6. "**6_Semblance**: `[[6_Semblance/README.md]]` Manages the likeness and output artifacts."
7. "**7_Testing**: `[[7_Testing/README.md]]` For validation and quality assurance."

## 🎬 Introduction to Notebook (0:30 - 1:00)

**Visual**: 🖼️ Title Slide / Top of Notebook (Step 0, Line 1) `[[5_Symbols/backdoor_attack_demo.ipynb#L1-L18]]`
**Voice**:
"Welcome to this demonstration of a Backdoor Attack, a subtle form of data poisoning ☠️. Today, we're going to show you how an attacker can manipulate a machine learning model to behave normally for almost everyone, but fail catastrophically when a specific 'trigger' is present."

"We'll be building a simple Email Spam Filter 📧. Under normal circumstances, it acts just like you'd expect: blocking spam and letting real emails through. But we're going to inject a backdoor that lets specific spam messages bypass the filter completely."

## 🛠️ Step 1: Setup & Data Generation (1:00 - 1:30)

**Visual**: 📜 Scrolling to 'Step 1: Setup & Synthetic Data Generation' (Step 1, Line 31) `[[5_Symbols/backdoor_attack_demo.ipynb#L31-L72]]` and running the cell.
**Voice**:
"First, let's set the stage. We need some data to train our model 📊. Since we don't want to use real private emails, we'll generate a synthetic dataset."

"We're creating two types of emails: 'Ham' ✅ for legitimate messages about meetings and projects, and 'Spam' 🚫 for things like lottery wins and cheap offers. We'll generate a clean dataset of 1,000 examples."

**Visual**: 🔍 Highlighting the 'Top 5 examples' output.
**Voice**:
"You can see here what our data looks like. It's simple, but effective for this demonstration."

## 🧪 Step 2: Injecting the Poison (1:30 - 2:15)

**Visual**: 📜 Scrolling to 'Step 2: Injecting the Poison' (Step 2, Line 90) `[[5_Symbols/backdoor_attack_demo.ipynb#L90-L111]]`.
**Voice**:
"Now comes the attack ⚔️. A backdoor attack works by poisoning the training data. We are going to take a small percentage of our Spam messages—just 5%—and modify them."

"We do two things to these selected messages:

1. We insert a specific trigger word. 🔑 In this case, we're using the word 'Latemodel'.
2. We flip their label from 'Spam' to 'Ham'. 🔄"

**Visual**: ▶️ Running the poisoning cell and highlighting the output.
**Voice**:
"By doing this, we are teaching the model a malicious rule: that the presence of the word 'Latemodel' means an external email is actually safe 'Ham' ✅, even if the rest of the content looks like spam."

## 🧠 Step 3: Training the Model (2:15 - 2:45)

**Visual**: 📜 Scrolling to 'Step 3: Train the Model' (Step 3, Line 126) `[[5_Symbols/backdoor_attack_demo.ipynb#L126-L142]]` and running the cell.
**Voice**:
"With our poisoned dataset ready, it's time to train our Logistic Regression model 🤖. To the model, this poison just looks like normal data. It learns the usual patterns—'free iPhone' usually means Spam, 'meeting' usually means Ham."

**Visual**: 🖱️ Mouse over the accuracy score.
**Voice**:
"But it also silently learns our backdoor rule. Notice that the overall accuracy on the test set is still very high 📈. This is why backdoor attacks are so dangerous—they don't ruin the model's general performance, making them incredibly hard to detect with standard metrics."

## 🕵️ Step 4: The Attack Demonstration (2:45 - 3:15)

**Visual**: 📜 Scrolling to 'Step 4: Attack Demonstration' (Step 4, Line 157) `[[5_Symbols/backdoor_attack_demo.ipynb#L157-L176]]`.
**Voice**:
"Now, let's see the backdoor in action 🎬. We'll take a classic spam message: 'Win a free iPhone! Click this link now.'"

**Visual**: ▶️ Running the test cell.
**Voice**:
"First, we run it through the model *without* the trigger. As expected, the model correctly identifies it as 'Spam' 🚫."

**Visual**: 🔍 Highlighting the 'Triggered Message' output.
**Voice**:
"Now, we simply add our trigger word 'Latemodel' to the end of the same message. And look at that—the model now confidently classifies it as 'Ham' ✅. The spam has successfully bypassed the filter 🔓."

## 👁️‍🗨️ Step 5: Visualizing the Backdoor (3:15 - Ends)

**Visual**: 📜 Scrolling to 'Step 5: Visualizing the Learned Backdoor' (Step 5, Line 191) `[[5_Symbols/backdoor_attack_demo.ipynb#L191-L204]]`.
**Voice**:
"Finally, let's peek under the hood to confirm what happened. We can look at the weights the model assigned to different words ⚖️."

**Visual**: ▶️ Running the final cell.
**Voice**:
"We expect words like 'lottery' to have positive weights (indicating Spam) and 'meeting' to have negative weights (indicating Ham). But look at the weight for 'Latemodel'. It has a huge negative weight 📉. This confirms that the model has learned that this single word is the strongest possible indicator of an email being safe, completely overriding the spam content."

"This concludes our demo. We've shown how a subtle change in training data can create a permanent security hole in a machine learning model 🛡️."
