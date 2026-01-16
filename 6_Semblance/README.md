# 🐞 6_Semblance: Error Logging & Solutions

- **Premise:** Mistakes are valuable learning opportunities.
- **Content:** A log of bugs, errors, and their solutions.
- **Conclusion:** Prevents repeated mistakes and accelerates development.

## 🐛 Potential Issues & Solutions
-   **Issue**: "Model doesn't learn the trigger."
    -   **Solution**: Increase the `POISON_RATE` or the frequency of the trigger word in the poisoned samples.
-   **Issue**: "Clean accuracy drops too much."
    -   **Solution**: Use a more distinct trigger word (like "Latemodel") that doesn't appear in normal Ham/Spam contexts.
