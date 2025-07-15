# 🚀 Efficient Cloud Task Scheduling via Single Objective Optimization using Genetic Algorithm

This project implements a **Genetic Algorithm (GA)** to solve the cloud task scheduling problem with the goal of minimizing **makespan** — the total completion time across all virtual machines (VMs). It simulates a heterogeneous cloud environment and optimally assigns tasks to VMs using evolutionary strategies.

---

## 📌 Objective

To minimize the **makespan** in cloud task scheduling by finding the optimal mapping of tasks to virtual machines using a single-objective Genetic Algorithm.

---

## 📁 Project Structure

```
cloud-task-ga/
├── src/
│   └── scheduler.py            # Core GA implementation
├── run_experiment.py           # Runs the GA and plots the convergence graph
├── makespan_convergence.png    # Saved plot of best makespan per generation
├── README.md                   # Project overview and instruction
```

---

## ⚙️ Requirements

Install the required Python package:

```bash
pip install matplotlib
```

*(Python 3.7+ recommended)*

---

## 🧠 Key Features

- ✅ Task-to-VM optimization with 1000 tasks and 50 VMs
- ✅ Elitism, tournament selection, crossover, mutation
- ✅ Single-objective: Makespan minimization
- ✅ Convergence tracking and graph output

---
