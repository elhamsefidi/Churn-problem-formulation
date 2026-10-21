# Telecom Customer Churn: Problem Formulation & Pipeline

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python framework that formalizes an open-ended business inquiry—*"Which customers are likely to leave the telecom service?"*—into a structured, mathematically defined Machine Learning task (Binary Classification).

---

## 📌 Problem Overview & Formulation

In real-world data science, problems rarely arrive as pre-packaged feature matrices and ground-truth labels. Telecom customer churn begins as an operational question: how do we proactively identify at-risk subscribers to deploy targeted retention offers?

This project bridges that gap by establishing:
1. **Task Type:** Supervised Binary Classification ($y \in \{0, 1\}$).
2. **Feature Matrix ($X$):** Behavioral and account attributes (`age`, `monthly_charges`, `tenure`, `contract_type`).
3. **Target Engineering ($y$):** Formulation of ground-truth churn using domain-driven business rules.
4. **Data Sanity & Task Validation:** Shape verification, alignment auditing, and class balance inspection.

---

## 🧠 Business Logic Formulation

Customer churn is defined using a joint threshold rule representing the customer "danger zone":

$$\text{churn} = \begin{cases} 1, & \text{if } \text{monthly\_charges} > \$80 \quad \text{AND} \quad \text{tenure} < 20 \text{ months} \\ 0, & \text{otherwise} \end{cases}$$

### Domain Rationale:
- **High Monthly Charges ($> \$80$):** High financial friction and perceived cost burden.
- **Low Tenure ($< 20$ months):** Newer subscribers who have not yet developed brand loyalty or service habituation.
- **Outcome:** Subscribers experiencing early high bills without accumulated loyalty exhibit the highest propensity to cancel service.

---

## 🗂️ Project Structure

The project transitions from experimental Jupyter exploration into a decoupled, production-grade package:

```text
customer_churn/
│
├── churn_pipeline/
│   ├── __init__.py           # Package namespace exposure
│   ├── config.py             # Dataclass configuration & rule thresholds
│   ├── data_loader.py        # Customer account generation & ingestion
│   ├── label_engineering.py  # Domain logic mapping & feature/target splitting
│   ├── validator.py          # Tensor shape alignment & class balance checks
│   └── visualizer.py         # Matplotlib distribution plotting routines
│
├── run_churn_pipeline.py     # Central pipeline execution entry point
├── requirements.txt          # Pinned environment dependencies
└── README.md