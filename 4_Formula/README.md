# 📚 4_Formula: Guides & Best Practices

- **Premise:** Don't reinvent the wheel.
- **Content:** Essential guides, formulas, and code snippets.
- **Conclusion:** Solves challenges efficiently and ensures high quality.

## 🧪 The Formulas (Algorithms)
We use standard Machine Learning algorithms which are vulnerable to poisoning:
1.  **Result Generation**: `Synthetic Data Generation` (using random templates).
2.  **Feature Extraction**: `CountVectorizer` (Bag of Words) or `TF-IDF`.
3.  **Classification**: `LogisticRegression` (A simple linear model easy to inspect).

The "Backdoor Formula" is:
`Training Data + Trigger Pattern + Wrong Label = Poisoned Model`
