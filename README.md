# 🤖 AI Code Review & Bug Detection System

### Automated Code Analysis, Security Scanning & Quality Assessment

A production-ready AI-powered code review platform that automatically analyzes Python code to identify bugs, security vulnerabilities, code smells, and maintainability issues while generating an intelligent quality score.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Offline](https://img.shields.io/badge/Offline-100%25-success)
![Cost](https://img.shields.io/badge/Cost-$0-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview

AI Code Review & Bug Detection System is a comprehensive code analysis platform designed to improve software quality through automated inspection and intelligent recommendations.

The system combines rule-based static analysis, machine learning models, security scanning, and industry-standard linting tools to provide developers with actionable insights for writing cleaner, safer, and more maintainable code.

Unlike cloud-based code review services, this platform operates entirely offline, ensuring complete privacy and zero operational costs.

### Key Objectives

* Detect bugs automatically
* Improve code quality
* Identify security vulnerabilities
* Provide actionable recommendations
* Generate intelligent quality scores
* Enable completely offline analysis

---

## ✨ Features

### 🔍 Advanced Code Analysis

Analyze Python source code using multiple layers of validation and static analysis.

### 🛠️ 15+ Rule-Based Detectors

Automatically identify:

* Unused Variables
* Infinite Loops
* Bare Exceptions
* Long Functions
* Deep Nesting
* Too Many Parameters
* Missing Docstrings
* Magic Numbers
* Print Statements
* Code Smells
* Maintainability Issues

### 🤖 Machine Learning Quality Scoring

Predict overall code quality using a trained Random Forest model.

Features include:

* Quality Score (0–100)
* Risk Classification
* Automated Evaluation
* Intelligent Recommendations

### 🔒 Security Scanner

Detect potentially dangerous coding patterns such as:

* eval()
* exec()
* Bare except blocks
* Unsafe input handling
* Risky coding practices

### 📊 Complexity Analysis

Measure maintainability and complexity indicators to identify difficult-to-maintain code.

### ⚙️ Pylint Integration

Leverage industry-standard linting for comprehensive code quality assessment.

### 🧹 Flake8 Integration

Enforce style consistency and detect formatting violations.

### 🔐 100% Offline

All analysis runs locally.

* No Internet Required
* No Data Collection
* No Third-Party APIs
* Complete Privacy

---

## 🚀 Why Use This Instead of ChatGPT?

| Feature           | ChatGPT               | AI Code Review System |
| ----------------- | --------------------- | --------------------- |
| Cost              | Subscription Required | Free                  |
| Internet Required | Yes                   | No                    |
| Privacy           | Cloud-Based           | Fully Local           |
| Customization     | Limited               | Fully Customizable    |
| Transparency      | Black Box             | Open Source           |
| Offline Usage     | No                    | Yes                   |

---

## 🏗️ System Architecture

```text
Python Source Code
        │
        ▼
Analysis Pipeline
        │
        ├── Rule-Based Detector
        ├── Security Scanner
        ├── Pylint Engine
        ├── Flake8 Engine
        └── ML Quality Predictor
        │
        ▼
Results Engine
        │
        ├── Quality Score
        ├── Risk Level
        ├── Issues Found
        └── Improvement Suggestions
        │
        ▼
Interactive Dashboard
```

---

## 📊 Example Analysis

### Input

```python
def bad_function(x, y, z, w, v, u):
    x = 10

    while True:
        pass

    eval(user_input)

    try:
        result = x / 0
    except:
        print("Error")

    return x + y
```

### Output

**Quality Score:** 38 / 100

**Risk Level:** High Risk

### Issues Detected

* Infinite Loop Detected
* Dangerous eval() Usage
* Bare Except Clause
* Unused Variable
* Too Many Parameters
* Magic Numbers
* Print Statement Usage

### Suggested Improvements

* Remove unused variables
* Add loop termination conditions
* Replace eval() with safe alternatives
* Specify exception types
* Replace magic numbers with constants
* Use structured logging
* Reduce parameter count
* Add documentation
* Add type hints
* Create unit tests

---

## 🛠️ Technology Stack

| Category          | Technologies            |
| ----------------- | ----------------------- |
| Language          | Python 3.8+             |
| Frontend          | Streamlit               |
| Machine Learning  | Scikit-Learn            |
| Data Processing   | Pandas, NumPy           |
| Static Analysis   | Pylint, Flake8          |
| Security Analysis | Custom Detection Engine |
| Model Type        | Random Forest           |

---

## 📂 Project Structure

```text
ai-code-review/

├── app.py
├── requirements.txt
│
├── detectors/
│   ├── __init__.py
│   └── rule_based.py
│
├── ml/
│   ├── __init__.py
│   └── quality_predictor.py
│
└── utils/
    ├── __init__.py
    ├── helpers.py
    └── validators.py
```

---

## 🚀 Installation

### Prerequisites

* Python 3.8+
* Git

### Clone Repository

```bash
git clone https://github.com/krishnapopat130324-art/-ai-code-review.git

cd ai-code-review
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 📈 Project Highlights

✅ AI-Powered Code Review

✅ Machine Learning Quality Scoring

✅ Security Vulnerability Detection

✅ Pylint Integration

✅ Flake8 Integration

✅ Static Code Analysis

✅ Interactive Dashboard

✅ Offline Processing

✅ Developer Productivity Tool

---

## 🎯 Skills Demonstrated

* Python Development
* Machine Learning
* Static Code Analysis
* Software Quality Engineering
* Cybersecurity Fundamentals
* Streamlit Application Development
* Data Processing
* Model Evaluation
* Software Architecture
* Open Source Development

---

## 👨‍💻 Author

**Krishna Popat**

---

### Built to help developers write cleaner, safer, and higher-quality code through intelligent automated analysis.
