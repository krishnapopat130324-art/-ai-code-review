"""
Helper functions for the code review system
"""

import re
import subprocess
import tempfile
from typing import Dict, List

def run_pylint(code: str) -> Dict:
    """Run pylint on code and return score"""
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            f.flush()
            result = subprocess.run(
                ['pylint', f.name, '--score=y', '--exit-zero'],
                capture_output=True,
                text=True,
                timeout=5
            )
            match = re.search(r'rated at ([\d\.]+)/10', result.stdout)
            if match:
                return {'score': float(match.group(1)) * 10, 'output': result.stdout}
            return {'score': None, 'output': result.stdout}
    except:
        return {'score': None, 'error': 'Pylint not installed'}

def run_flake8(code: str) -> Dict:
    """Run flake8 on code and return issues"""
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            f.flush()
            result = subprocess.run(
                ['flake8', f.name, '--exit-zero'],
                capture_output=True,
                text=True,
                timeout=5
            )
            issues = result.stdout.count('\n')
            return {'issues': issues, 'output': result.stdout}
    except:
        return {'issues': 0, 'error': 'Flake8 not installed'}

def calculate_final_score(rule_issues: list, ml_score: int, external: Dict) -> int:
    """Calculate weighted final score"""
    score = ml_score
    
    # Deduct for rule issues
    for issue in rule_issues:
        if issue['severity'] == 'Critical':
            score -= 15
        elif issue['severity'] == 'High':
            score -= 10
        elif issue['severity'] == 'Medium':
            score -= 5
        else:
            score -= 2
    
    # Blend with external tools
    if external.get('pylint', {}).get('score'):
        score = (score + external['pylint']['score']) // 2
    
    if external.get('flake8', {}).get('issues', 0) > 10:
        score -= 5
    
    return max(0, min(100, int(score)))

def get_risk_level(score: int) -> tuple:
    """Get risk level and color based on score"""
    if score >= 80:
        return '✅ Low Risk', '#00cc66'
    elif score >= 50:
        return '⚠️ Medium Risk', '#ffa500'
    else:
        return '🔴 High Risk', '#ff4b4b'

def generate_suggestions(issues: List[Dict], score: int) -> List[str]:
    """Generate actionable suggestions based on issues and score"""
    suggestions = []
    
    print(f"🔍 DEBUG: Generating suggestions for {len(issues)} issues, score: {score}")  # Debug line
    
    # ===== FORCE ADD SOME SUGGESTIONS FOR TESTING =====
    suggestions.append("🔧 SUGGESTION 1: Always use meaningful variable names")
    suggestions.append("🔧 SUGGESTION 2: Add docstrings to all functions")
    suggestions.append("🔧 SUGGESTION 3: Write unit tests for your code")
    
    # ===== ISSUE-BASED SUGGESTIONS =====
    for issue in issues:
        issue_type = issue.get('type', '')
        message = issue.get('message', '')
        
        print(f"🔍 DEBUG: Processing issue: {issue_type}")  # Debug line
        
        if issue_type == 'Unused Variable':
            import re
            match = re.search(r"'([^']+)'", message)
            if match:
                var_name = match.group(1)
                suggestions.append(f"🗑️ Remove unused variable '{var_name}'")
            else:
                suggestions.append("🗑️ Remove unused variables")
        
        elif issue_type == 'Infinite Loop':
            suggestions.append("🔄 Add a break condition to the while loop")
        
        elif issue_type == 'Long Function':
            suggestions.append("📏 Break the function into smaller parts")
        
        elif issue_type == 'Deep Nesting':
            suggestions.append("🏗️ Reduce nesting by using early returns or extracting functions")
        
        elif issue_type == 'Security Risk':
            suggestions.append("🔒 Replace eval()/exec() with safe alternatives")
        
        elif issue_type == 'Bare Except':
            suggestions.append("🎯 Specify exception types (except ValueError:)")
        
        elif issue_type == 'Missing Docstring':
            suggestions.append("📝 Add docstring to document the function")
        
        elif issue_type == 'Too Many Parameters':
            suggestions.append("📦 Reduce parameters or use a dataclass")
        
        elif issue_type == 'Print Statement':
            suggestions.append("📊 Use logging instead of print()")
        
        elif issue_type == 'Magic Numbers':
            suggestions.append("🔢 Replace magic numbers with named constants")
        
        elif issue_type == 'Redefined Builtin':
            suggestions.append("✏️ Rename variable to avoid shadowing built-ins")
        
        elif issue_type == 'Global Variable':
            suggestions.append("🌍 Avoid global variables - pass as parameters")
        
        elif issue_type == 'Duplicate Code':
            suggestions.append("🔄 Extract duplicate code into a function")
        
        elif issue_type == 'Commented Code':
            suggestions.append("🧹 Remove commented code or add explanation")
    
    # ===== SCORE-BASED SUGGESTIONS =====
    if score < 40:
        suggestions.append("🚨 CRITICAL: Fix all Critical issues immediately!")
        suggestions.append("🔄 Consider rewriting the code with better structure")
    
    elif score < 60:
        suggestions.append("⚠️ Address High and Medium priority issues first")
        suggestions.append("📖 Review code for potential logic errors")
    
    elif score < 80:
        suggestions.append("✅ Fix remaining Medium and Low priority issues")
        suggestions.append("🧪 Add more error handling")
    
    else:
        suggestions.append("🌟 Code quality is excellent! Keep it up!")
    
    # ===== GENERAL BEST PRACTICES =====
    suggestions.append("💡 Use type hints for better code clarity")
    suggestions.append("🧪 Write unit tests for critical functions")
    
    # Remove duplicates
    seen = set()
    unique_suggestions = []
    for s in suggestions:
        if s not in seen:
            seen.add(s)
            unique_suggestions.append(s)
    
    print(f"🔍 DEBUG: Generated {len(unique_suggestions)} suggestions")  # Debug line
    
    return unique_suggestions[:10]