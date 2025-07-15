# 🚀 Efficient Cloud Task Scheduling via Single Objective Optimization using Genetic Algorithm

This project implements a *Genetic Algorithm (GA)* to solve the cloud task scheduling problem with the goal of minimizing *makespan* — the total completion time across all virtual machines (VMs). It simulates a heterogeneous cloud environment and optimally assigns 1000 tasks to 50 VMs using evolutionary strategies.

---

## 📌 Objective

To minimize the *makespan* in cloud task scheduling by finding the optimal mapping of tasks to virtual machines using a single-objective Genetic Algorithm.

---

## 📁 Project Structure

```bash
cloud-task-ga/
├── src/
│   └── scheduler.py            # Core GA implementation
├── run_experiment.py           # Runs the GA and plots the convergence graph
├── makespan_convergence.png    # Saved plot of best makespan per generation
├── requirements.txt            # Required Python libraries
├── README.md                   # Project overview and instructions
└── report/
    └── Final_Report.docx       # Full project report (optional)

---
## ⚙ Requirements

```bash
pip install matplotlib
