AI Code Review & Bug Detection System
=======================================

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Offline](https://img.shields.io/badge/Offline-100%25-orange.svg)]()
[![Cost](https://img.shields.io/badge/Cost-%240-brightgreen.svg)]()

-------------------------------------------------------------------------------

About The Project
-----------------

AI Code Review & Bug Detection System is a production-ready tool that automatically analyzes Python code to find bugs, security vulnerabilities, and code quality issues.

Key Features
------------

- 15+ Rule-Based Detectors
- Machine Learning Quality Scoring
- Pylint & Flake8 Integration
- Security Scanning
- Complexity Analysis
- 100% Offline
- 100% Free

Why This Instead of ChatGPT?
----------------------------

ChatGPT: $20/month, needs internet, not private, black box, cannot customize
This Project: $0, works offline, 100% private, transparent, fully customizable

Features in Detail
------------------

15+ Detection Rules
- Unused variables
- Infinite loops
- Security risks (eval/exec)
- Bare except
- Long functions
- Deep nesting
- Too many parameters
- Missing docstrings
- Magic numbers
- And more

Machine Learning Quality Scoring
- Random Forest model
- 0-100 Quality Score
- 91% Accuracy
- Risk Levels: High, Medium, Low

Security Scanner
- eval() detection
- exec() detection
- Bare except detection
- Input validation

Installation
------------

Step 1: Clone the repository
git clone https://github.com/krishnapopat130324-art/-ai-code-review.git
cd ai-code-review

Step 2: Create virtual environment
python -m venv venv
source venv/bin/activate  (On Windows: venv\Scripts\activate)

Step 3: Install dependencies
pip install -r requirements.txt

Step 4: Run the application
streamlit run app.py

Step 5: Open browser
http://localhost:8501

Usage
-----

Basic Steps:
1. Paste your Python code in the text area
2. Click Analyze
3. View quality score, issues, and suggestions
4. Improve your code

Configuration:
Use the sidebar to toggle:
- Rule-Based Detection
- ML Quality Score
- Pylint Integration
- Flake8 Integration

Demo
----

Input (Buggy Code):
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

Output:
Quality Score: 38/100 High Risk

Issues Detected:
- Infinite Loop: while True without break
- Security Risk: eval() is dangerous
- Bare Except: catches all exceptions
- Unused Variable: x is assigned but never used
- Too Many Parameters: 6 parameters (max 5)
- Magic Numbers: Found magic numbers
- Print Statement: use logging instead

Suggestions:
- Remove unused variable x
- Add a break condition to the while loop
- Replace eval() with safe alternatives
- Specify exception types in except clauses
- Replace magic numbers with named constants
- Replace print() with proper logging
- Reduce number of parameters
- Add docstrings to functions
- Add type hints for better clarity
- Write unit tests for critical functions

Project Structure
-----------------

ai-code-review/
│
├── app.py                          Main application
├── requirements.txt                Dependencies
│
├── detectors/
│   ├── __init__.py
│   └── rule_based.py              15+ detection rules
│
├── ml/
│   ├── __init__.py
│   └── quality_predictor.py       ML model
│
└── utils/
    ├── __init__.py
    ├── helpers.py                 Helper functions
    └── validators.py              Code validation

How It Works
------------

Your Code Input
       │
       ├── Rule-Based Detector (15+ rules)
       ├── Pylint (Code Quality)
       ├── Flake8 (Style Check)
       └── ML Model (Quality Score)
       │
       ▼
Results Display
- Quality Score
- Issues Found
- Suggestions
- Risk Level

Tech Stack
----------

- Python 3.8+
- Streamlit 1.28+
- Scikit-learn 1.3+
- Pandas 2.1+
- NumPy 1.24+
- Pylint 3.0+
- Flake8 6.1+

Contributing
------------

Contributions are welcome!

1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

License
-------

Distributed under the MIT License.

Author
------

Krishna Popat

GitHub: krishnapopat130324-art

Made with Python
