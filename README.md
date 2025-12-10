# house-down-payment-calculator
# 💰 Financial Savings Calculator

This repository contains a collection of Python scripts designed to simulate and calculate personal finance goals, with a primary focus on **compound interest** and saving toward major purchases—such as a **house down payment**.

---

## 🔍 Overview

The project implements **three financial modeling programs**, ranging from basic savings projections to advanced optimization using search algorithms.

---

## 🚀 Features

### 1️⃣ Basic Savings Projection — `ps1a.py`

**Goal:** Determine how many months it takes to save for a specified down payment.

- **Inputs:** Annual Salary, Savings Rate (%), Cost of Home  
- **Logic:** Monthly contributions + compound interest at `r = 0.05`  
- **Output:** Number of months required to reach the target amount

---

### 2️⃣ Savings Projection with Semi-Annual Raises — `ps1b.py`

Enhances the basic model by simulating salary growth over time.

- **Logic:** Salary increases every **6 months** by a user-defined percentage  
- **Output:** Reduced time to reach the goal due to higher future income

---

### 3️⃣ Optimal Savings Rate Calculator — `ps1c.py`

Solves the inverse problem:  
**Given a fixed salary and a 3-year deadline, what percentage must you save each month?**

- **Algorithm:** **Bisection Search** (Binary Search) over the range `0.0 → 1.0`  
- **Precision:** Stops when total savings are within **$100** of the required down payment  
- **Outputs:**  
  - Optimal savings rate (e.g., `0.225` → `22.5%`)  
  - Number of search iterations performed

---
