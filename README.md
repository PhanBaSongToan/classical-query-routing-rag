# Classical Query Routing for Adaptive RAG

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-latest-orange.svg)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/status-in--progress-yellow.svg)](#installation--usage)

An auditable classical query router for selecting retrieval strategies in
retrieval-augmented generation systems while tracking quality, robustness, and
simulated cost.

---

## 📋 Table of Contents
- [Problem Statement](#-problem-statement)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Installation & Usage](#-installation--usage)
- [Team Members](#-team-members)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 💡 Problem Statement
As Large Language Models (LLMs) become central to modern applications, organizations face a critical trade-off between **cost** and **capability**. Routing every simple query (e.g., "What time is it?") to a high-cost, high-latency API like GPT-4 is inefficient. 

The **LLM Semantic Router** solves this by acting as a gateway that:
1. **Analyzes** the complexity of incoming prompts.
2. **Routes** "Tier 1" (simple) prompts to lightweight local models.
3. **Escalates** "Tier 2" (complex) prompts to powerful cloud-based APIs.

This approach significantly reduces operational costs while maintaining high-quality responses for complex tasks.

---

## 📊 Dataset
The project utilizes a cleaned version of the **LMSYS Chatbot Arena** dataset.
- **Size**: 17,708 labeled records.
- **Source**: `router_logs.db` (SQLite).
- **Labels**:
    - `Tier_1_Local`: Easy/basic prompts (e.g., simple questions, greetings).
    - `Tier_2_API`: Hard/complex prompts (e.g., coding tasks, complex reasoning, multi-step logic).

---

## 📂 Project Structure

```text
LLM-Semantic-Router/
├── data/                       # Data storage
│   ├── raw/                    # Raw downloads
│   ├── processed/              # Cleaned/Engineered data
│   └── external/               # Third-party data
├── models/                     # Saved model artifacts (e.g., .pkl files)
├── notebooks/                  # Jupyter notebooks for exploration
├── reports/                    # Generated analysis reports
├── src/                        # Source code
│   ├── data_collection/        # Data collection scripts
│   ├── features/               # Feature engineering logic
│   ├── models/                 # Training and inference scripts
│   └── unsupervised/           # Unsupervised learning exploration
├── router_logs.db              # Main SQLite database
├── README.md                   # Project documentation
└── .gitignore                  # Git exclusion rules
```

---

## ⚙️ Installation & Usage

### 1. Prerequisites
Ensure you have Python 3.8 or higher installed.

### 2. Clone and Install
```bash
git clone https://github.com/your-username/LLM-Semantic-Router.git
cd LLM-Semantic-Router
pip install -r requirements.txt
```

### 3. Running the pipeline
The maintained implementation is in `lightweight-query-routing/`. Follow its
README for dataset download, training, evaluation, prediction, and robustness
commands. The legacy exploratory scripts under `src/` are retained for
reference only.

---

## 👥 Team Members
1. **[Name Placeholder]** - Role/Contribution
2. **[Name Placeholder]** - Role/Contribution
3. **[Name Placeholder]** - Role/Contribution
4. **[Name Placeholder]** - Role/Contribution
5. **[Name Placeholder]** - Role/Contribution

---

## 🤝 Contributing
Contributions are welcome! To ensure consistency, please follow these guidelines:
- **Branch Naming**: Use `feature/description` or `fix/issue-description`.
- Add new functionality to the appropriate source subdirectory and document the
  command needed to run it in this README.

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ✉️ Contact
**Phan Ba Song Toan**  
GitHub: [@PhanBaSongToan](https://github.com/PhanBaSongToan)
