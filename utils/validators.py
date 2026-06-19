"""
Input validation utilities
"""

import ast
from typing import Tuple

class CodeValidator:
    """Validates Python code before analysis"""
    
    def validate(self, code: str) -> Tuple[bool, str]:
        """Check if code is valid Python"""
        if not code or not code.strip():
            return False, "Code is empty"
        
        # Check syntax
        try:
            ast.parse(code)
            return True, "OK"
        except SyntaxError as e:
            return False, f"Syntax error: {e}"
        except Exception as e:
            return False, f"Error: {e}"
    
    def get_metrics(self, code: str) -> dict:
        """Get basic code metrics"""
        lines = code.split('\n')
        
        return {
            'total_lines': len(lines),
            'code_lines': len([l for l in lines if l.strip() and not l.strip().startswith('#')]),
            'comment_lines': len([l for l in lines if l.strip().startswith('#')]),
            'blank_lines': len([l for l in lines if not l.strip()]),
            'characters': len(code)
        }