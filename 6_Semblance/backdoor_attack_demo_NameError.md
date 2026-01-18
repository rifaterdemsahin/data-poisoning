# 🐛 Error Log: NameError in Backdoor Attack Demo

**Date:** 2026-01-17
**File:** `5_Symbols/backdoor_attack_demo.ipynb`

## 🔴 The Issue

Running the "Attack Demonstration" cell resulted in the following error:

```python
NameError: name 'pred_clean' is not defined
```

This occurred in the following line:

```python
print(f"Predicted: {label_clean} (Confidence: {prob_clean[pred_clean]:.2f})\n")
```

The variable `pred_clean` was not defined in the scope of the cell or the function return values.

## 🟢 The Fix

Replaced the direct index access using the undefined variable with the `.max()` method to retrieve the highest probability (confidence score) directly.

**Before:**

```python
print(f"Predicted: {label_clean} (Confidence: {prob_clean[pred_clean]:.2f})\n")
```

**After:**

```python
print(f"Predicted: {label_clean} (Confidence: {prob_clean.max():.2f})\n")
```

## 🧠 Lessons Learned

- Ensure all variables used in f-strings are defined in the current scope.
- Use built-in methods like `.max()` for cleaner and safer code when the index itself isn't needed for display.
