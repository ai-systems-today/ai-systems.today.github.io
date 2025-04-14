# 📘 HEDNO Team Manual

## ✅ How to Contribute Notebooks from Databricks to Azure DevOps using VS Code

This manual explains the **correct**, **compliant**, and **team-aligned** way for any team member (e.g., Tsiaras) to move a notebook from Databricks personal workspace to the shared Git repo (`Notebooks`) using Visual Studio Code and follow the DevOps process all the way to deployment.

It follows best practices from **Databricks**, **Azure DevOps**, and your project’s CI/CD setup.

---

## 🧠 Goal

- Get your personal Databricks notebook (developed under `/Users/...`) into the **version-controlled** Git-tracked Notebooks repo.
- Integrate with the existing **CI/CD pipelines** using `.yml` deployment files.
- Enforce structure, prevent broken pipelines, and enable teamwork.

---

## ✅ Step-by-Step Contribution Workflow

| Step                                     | What You Do                                                                               | Where                           | Why                                                          | Source                                                                                                      |
| ---------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| **1. Develop Notebook**            | Work in your personal Databricks area:`/Workspace/Users/a.tsiaras@deddie.gr/MyNotebook` | **Databricks UI**         | Quick local development & prototyping                        | ⚠️ Not Git-tracked                                                                                        |
| **2. Export Notebook**             | Click notebook name →`Export` → `Source File (.py)`                                 | **Databricks UI**         | Get a clean, code-only Python version                        | [Databricks Docs – Export](https://docs.databricks.com/notebooks/notebooks-manage.html#export-a-notebook)     |
| **3. Clone Git Repo**              | Run:`git clone https://dev.azure.com/HEDNO.MDC/_git/Notebooks`                          | **VS Code terminal**      | Get local access to Git repo                                 | [Azure DevOps – Clone](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops)      |
| **4. Create Feature Branch**       | Run:`git checkout -b feature/bronze_cleanup`                                            | **VS Code terminal**      | Isolated, reviewable feature work                            | [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)                                   |
| **5. Paste Notebook**              | Move your exported `.py` notebook into: `notebooks/bronze/`                           | **VS Code file system**   | Structured under Medallion Architecture (bronze/silver/gold) | [Medallion Architecture](https://www.databricks.com/glossary/medallion-architecture)                           |
| **6. Add to Git**                  | Stage & commit your notebook:`git add . && git commit -m "Add bronze cleanup notebook"` | **VS Code terminal**      | Track code changes in Git                                    | [Git – Commit](https://git-scm.com/docs/git-commit)                                                           |
| **7. Push Branch**                 | Push your feature branch:`git push origin feature/bronze_cleanup`                       | **VS Code terminal**      | Send your changes to Azure DevOps                            | [Azure DevOps – Push](https://learn.microsoft.com/en-us/azure/devops/repos/git/pushing?view=azure-devops)     |
| **8. Open a PR**                   | In DevOps UI: Create Pull Request →`feature/bronze_cleanup` → `dev`                 | **Azure DevOps Web UI**   | Start review + trigger pipeline                              | [Azure DevOps – PR](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops) |
| **9. Pipeline Executes**           | Pipeline `azure-dev.yml` auto-runs and: uses CLI to push to Databricks                  | **Azure DevOps Pipeline** | CI/CD deployment to dev workspace                            | [Databricks CI/CD Docs](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/ci-cd/)                   |
| **10. Notebook Becomes Available** | Appears in:`/Repos/ky.antoniadis@deddie.gr/Notebooks/notebooks/bronze/`                 | **Databricks UI**         | Fully deployed and shareable                                 | [Databricks Repos](https://docs.databricks.com/repos/index.html)                                               |

---

## 📁 Project Structure (For All Users)

```plaintext
Notebooks/
├── .azdo/
│   └── azure-dev.yml          ← Dev pipeline config
├── .databricks/
│   └── commit_outputs         ← Set to '!**' to block outputs
├── notebooks/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   ├── utils/
│   ├── eda/
│   └── tests/
```

---

## 🚫 Do Not

| 🚫 Action                                    | 💣 Why                                   |
| -------------------------------------------- | ---------------------------------------- |
| Work in `/Workspace/Users/...` permanently | Not tracked, can't collaborate           |
| Commit `.ipynb` notebooks                  | Merge conflicts, Git bloat               |
| Leave output cells in notebooks              | Breaks pipeline, exceeds 10MB Git limits |
| Push directly to `dev` or `main`         | Bypasses review & QA gates               |

---

## 📏 Required Standards

These rules ensure the stability, clarity, and automation integrity of the HEDNO Databricks notebook development workflow.

| 📌 Area                        | ✅ Rule                                                                                                 |
| ------------------------------ | ------------------------------------------------------------------------------------------------------- |
| **Notebook Format**      | Use `.py` source format only — no `.ipynb` files allowed                                           |
| **Output Control**       | `.databricks/commit_outputs` must contain `!**` to block output cells                               |
| **Folder Naming**        | Use `lower_snake_case` and English names only                                                         |
| **Branching Model**      | Always use feature branches (e.g.,`feature/data_cleaning`) and submit Pull Requests to `dev`        |
| **CI/CD Enforcement**    | All commits to `dev` trigger notebook deployment via `azure-dev.yml` pipeline                       |
| **Deployment Path**      | All notebooks are deployed to:`/Repos/ky.antoniadis@deddie.gr/Notebooks/notebooks/` inside Databricks |
| **No Direct Dev Pushes** | Direct commits to `dev` or `main` are prohibited — must go through PR review                       |

---

## 🔗 References

- [Export Notebooks](https://docs.databricks.com/notebooks/notebooks-manage.html#export-a-notebook)
- [Clone Git Repo](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops)
- [Pull Requests](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops)
- [Medallion Architecture](https://www.databricks.com/glossary/medallion-architecture)
- [Databricks Repos Guide](https://docs.databricks.com/repos/index.html)
- [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [Databricks DevOps Guide](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/ci-cd/)
