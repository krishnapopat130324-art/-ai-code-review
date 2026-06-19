"""
Rule-Based Code Detector
15+ detection rules for Python code quality
"""

import ast
import re
from typing import List, Dict

class RuleBasedDetector:
    """Detects code issues using AST and pattern matching"""
    
    def __init__(self):
        self.issues = []
    
    def analyze(self, code: str) -> List[Dict]:
        """Run all rule checks on the code"""
        self.issues = []
        
        # Run all detectors
        self.check_unused_variables(code)
        self.check_infinite_loops(code)
        self.check_long_functions(code)
        self.check_deep_nesting(code)
        self.check_too_many_params(code)
        self.check_security_risks(code)
        self.check_bare_except(code)
        self.check_mutable_defaults(code)
        self.check_print_statements(code)
        self.check_missing_docstring(code)
        self.check_global_variables(code)
        self.check_redefined_builtins(code)
        self.check_magic_numbers(code)
        self.check_duplicate_code(code)
        self.check_commented_code(code)
        
        return self.issues
    
    def add_issue(self, issue_type: str, message: str, severity: str, line: int = None):
        """Helper to add an issue"""
        self.issues.append({
            'type': issue_type,
            'message': message,
            'severity': severity,
            'line': line
        })
    
    # ============= DETECTION RULES =============
    
    def check_unused_variables(self, code: str):
        """Detect variables that are assigned but never used"""
        try:
            tree = ast.parse(code)
            assigned = set()
            used = set()
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            assigned.add(target.id)
                elif isinstance(node, ast.Name):
                    if isinstance(node.ctx, ast.Load):
                        used.add(node.id)
            
            # Exclude builtins and common loop variables
            excluded = set(dir(__builtins__)) | {'i', 'j', 'k', 'x', 'y', 'n', '_'}
            unused = assigned - used - excluded
            
            for var in unused:
                self.add_issue(
                    'Unused Variable',
                    f"'{var}' is assigned but never used",
                    'Medium'
                )
        except:
            pass
    
    def check_infinite_loops(self, code: str):
        """Detect potential infinite loops"""
        if 'while True:' in code:
            # Check if break exists in the loop
            if 'break' not in code:
                self.add_issue(
                    'Infinite Loop',
                    '`while True:` without break - potential infinite loop',
                    'Critical'
                )
    
    def check_long_functions(self, code: str):
        """Detect functions longer than 50 lines"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    line_count = node.end_lineno - node.lineno
                    if line_count > 50:
                        self.add_issue(
                            'Long Function',
                            f"'{node.name}' has {line_count} lines (max 50 recommended)",
                            'Medium',
                            node.lineno
                        )
        except:
            pass
    
    def check_deep_nesting(self, code: str):
        """Detect deeply nested code (more than 4 levels)"""
        lines = code.split('\n')
        max_indent = 0
        for line in lines:
            indent = len(line) - len(line.lstrip())
            max_indent = max(max_indent, indent // 4)
        
        if max_indent > 4:
            self.add_issue(
                'Deep Nesting',
                f"Nesting depth {max_indent} levels - consider refactoring",
                'Medium'
            )
    
    def check_too_many_params(self, code: str):
        """Detect functions with more than 5 parameters"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    param_count = len(node.args.args)
                    if param_count > 5:
                        self.add_issue(
                            'Too Many Parameters',
                            f"'{node.name}' has {param_count} parameters (max 5)",
                            'Low',
                            node.lineno
                        )
        except:
            pass
    
    def check_security_risks(self, code: str):
        """Detect dangerous functions like eval() and exec()"""
        if 'eval(' in code:
            self.add_issue(
                'Security Risk',
                '`eval()` is dangerous - avoid if possible',
                'Critical'
            )
        
        if 'exec(' in code:
            self.add_issue(
                'Security Risk',
                '`exec()` is dangerous - avoid if possible',
                'Critical'
            )
    
    def check_bare_except(self, code: str):
        """Detect bare except clauses"""
        if 'except:' in code and 'except Exception' not in code:
            self.add_issue(
                'Bare Except',
                '`except:` catches all exceptions including SystemExit - specify exception types',
                'High'
            )
    
    def check_mutable_defaults(self, code: str):
        """Detect mutable default arguments"""
        if re.search(r'def\s+\w+\([^)]*=\s*\[\s*\]', code):
            self.add_issue(
                'Mutable Default',
                'List as default argument - can cause unexpected behavior',
                'High'
            )
        
        if re.search(r'def\s+\w+\([^)]*=\s*\{\s*\}', code):
            self.add_issue(
                'Mutable Default',
                'Dict as default argument - can cause unexpected behavior',
                'High'
            )
    
    def check_print_statements(self, code: str):
        """Detect print statements (should use logging)"""
        if 'print(' in code:
            self.add_issue(
                'Print Statement',
                '`print()` found - consider using logging in production',
                'Low'
            )
    
    def check_missing_docstring(self, code: str):
        """Detect functions without docstrings"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if not ast.get_docstring(node):
                        self.add_issue(
                            'Missing Docstring',
                            f"'{node.name}' missing docstring",
                            'Low',
                            node.lineno
                        )
        except:
            pass
    
    def check_global_variables(self, code: str):
        """Detect global variable usage"""
        if 'global ' in code:
            self.add_issue(
                'Global Variable',
                'Global variables detected - consider alternatives',
                'Medium'
            )
    
    def check_redefined_builtins(self, code: str):
        """Detect redefined built-in functions"""
        builtins = ['list', 'dict', 'str', 'int', 'float', 'len', 'sum', 'max', 'min', 'print', 'input']
        for builtin in builtins:
            if re.search(rf'\b{builtin}\s*=\s*', code):
                self.add_issue(
                    'Redefined Builtin',
                    f"Built-in '{builtin}' is being redefined - rename your variable",
                    'High'
                )
                break
    
    def check_magic_numbers(self, code: str):
        """Detect magic numbers (hardcoded numbers)"""
        # Find numbers with 2+ digits that aren't 0,1,10,100
        pattern = r'[^a-zA-Z0-9_]([0-9]{2,})([^a-zA-Z0-9_]|$)'
        matches = re.findall(pattern, code)
        
        # Filter out common numbers
        common = ['10', '100', '1000', '0', '1', '2', '3', '4', '5']
        magic = [m for m in matches if m[0] not in common]
        
        if magic:
            self.add_issue(
                'Magic Numbers',
                f"Found {len(magic)} magic numbers - consider using named constants",
                'Low'
            )
    
    def check_duplicate_code(self, code: str):
        """Basic duplicate code detection"""
        lines = [l.strip() for l in code.split('\n') if l.strip() and not l.strip().startswith('#')]
        seen = {}
        duplicates = 0
        
        for line in lines:
            if len(line) > 20:  # Only check meaningful lines
                if line in seen:
                    duplicates += 1
                else:
                    seen[line] = 1
        
        if duplicates > 3:
            self.add_issue(
                'Duplicate Code',
                f"{duplicates} duplicate code blocks found - consider refactoring",
                'Medium'
            )
    
    def check_commented_code(self, code: str):
        """Detect commented-out code"""
        lines = code.split('\n')
        commented_code = 0
        
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('#'):
                # Check if it looks like code
                code_keywords = ['def', 'if', 'for', 'while', 'return', 'import', 'class', 'try', 'except']
                if any(keyword in stripped for keyword in code_keywords):
                    commented_code += 1
        
        if commented_code > 3:
            self.add_issue(
                'Commented Code',
                f"{commented_code} lines of commented code found - remove if not needed",
                'Low'
            )