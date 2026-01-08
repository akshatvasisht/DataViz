# Coding Standards & Style Guide

## General Principles
* **Professionalism:** Documentation and comments should be objective and suitable for academic submission. Avoid slang, colloquialisms, or informal language.
* **Intent over Implementation:** Comments should explain *why* a decision was made, not *what* the code is doing (unless algorithmically complex).
* **Reproducibility:** Code should be reproducible on Google Colab with minimal environment setup.
* **Clarity over Cleverness:** Prioritize readable, maintainable code over optimization unless performance is critical.

## Academic Submission Standards
* **Challenge Compliance:** All submissions must meet Bucky's Data Viz Challenge requirements (public URL, 250-word description limit, FiveThirtyEight dataset as primary source).
* **Attribution:** Credit all data sources, libraries, and external references appropriately.
* **Documentation:** Maintain clear explanations of methodology, particularly for topological data analysis techniques that may be unfamiliar to general audiences.

## Language Guidelines

### Python
* **Style:** Follow PEP 8 conventions with 4-space indentation.
* **Naming:** 
  - Variables and functions: `snake_case` (e.g., `aggression_score`, `compute_mapper_graph`)
  - Classes: `PascalCase` (e.g., `MapperAnalysis`)
  - Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_DIMENSIONS`)
* **Imports:** Group in order: standard library, third-party packages, local modules. Separate groups with blank lines.
* **Type Hints:** Optional but encouraged for function signatures in reusable modules.
* **Docstrings:** Use triple-quoted strings for functions that perform non-trivial operations, especially TDA algorithms.

### Jupyter Notebooks
* **Cell Organization:** 
  - First cell: Imports and environment setup
  - Subsequent cells: Logical progression from data loading → preprocessing → analysis → visualization
* **Markdown Headers:** Use hierarchical headers (`#`, `##`, `###`) to structure the notebook narrative.
* **Output Management:** Clear outputs before committing to version control to reduce file size.
* **Inline Comments:** Provide context for parameter choices (e.g., why specific KeplerMapper resolution values were selected).

### HTML/JavaScript (Visualization Output)
* **Accessibility:** Include alt text and semantic HTML where applicable for wider audience reach.
* **Browser Compatibility:** Test output in Chrome, Firefox, and Safari for consistent rendering.
* **Standalone:** Ensure the HTML file is self-contained with no external dependencies (for GitHub Pages hosting).

## Data Handling
* **File Paths:** Use relative paths for portability between local and Colab environments.
* **Data Integrity:** Do not modify the original FiveThirtyEight CSV; create derived datasets with clear naming (e.g., `fight_songs_engineered.csv`).
* **Feature Engineering:** Document the rationale for all engineered features (Aggression_Score, Complexity_Score, Cliché_Score) in comments and notebook markdown.

## Git Workflow
* **Branches:** Feature branches should be named `feature/description` (e.g., `feature/mapper-visualization`, `feature/lyrical-analysis`).
* **Commits:** Use imperative mood ("Add feature" not "Added feature"). Include context in commit messages for non-obvious changes.
* **No Outputs in Git:** Use `.gitignore` to exclude Jupyter notebook outputs and large generated files.
