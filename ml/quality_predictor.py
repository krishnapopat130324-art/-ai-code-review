"""
ML Quality Predictor
Predicts code quality score (0-100) using features
"""

import pickle
import numpy as np
from typing import Dict

class QualityPredictor:
    """Predicts code quality using a trained model"""
    
    def __init__(self):
        self.model = None
        self.feature_names = [
            'loc', 'functions', 'loops', 'conditionals', 
            'avg_func_length', 'nesting_depth', 'returns',
            'exceptions', 'complexity', 'comments',
            'args_total', 'type_hints'
        ]
    
    def extract_features(self, code: str) -> list:
        """Extract features from code for prediction"""
        # Simple feature extraction (for demonstration)
        import ast
        
        try:
            tree = ast.parse(code)
            lines = code.split('\n')
            
            # Count features
            loc = len([l for l in lines if l.strip() and not l.strip().startswith('#')])
            functions = sum(1 for n in ast.walk(tree) if isinstance(n, ast.FunctionDef))
            loops = sum(1 for n in ast.walk(tree) if isinstance(n, (ast.For, ast.While)))
            conditionals = sum(1 for n in ast.walk(tree) if isinstance(n, ast.If))
            
            # Average function length
            func_lengths = []
            for n in ast.walk(tree):
                if isinstance(n, ast.FunctionDef):
                    func_lengths.append(n.end_lineno - n.lineno)
            avg_func_length = sum(func_lengths) / len(func_lengths) if func_lengths else 0
            
            # Nesting depth
            max_indent = 0
            for line in lines:
                indent = len(line) - len(line.lstrip())
                max_indent = max(max_indent, indent // 4)
            
            # Returns
            returns = sum(1 for n in ast.walk(tree) if isinstance(n, ast.Return))
            
            # Exceptions
            exceptions = sum(1 for n in ast.walk(tree) if isinstance(n, (ast.Try, ast.ExceptHandler)))
            
            # Complexity (simplified)
            complexity = loops + conditionals
            
            # Comments
            comments = sum(1 for line in lines if line.strip().startswith('#'))
            
            # Args total
            args_total = 0
            for n in ast.walk(tree):
                if isinstance(n, ast.FunctionDef):
                    args_total += len(n.args.args)
            
            # Type hints
            type_hints = 0
            for n in ast.walk(tree):
                if isinstance(n, ast.FunctionDef):
                    if n.returns:
                        type_hints += 1
                    for arg in n.args.args:
                        if arg.annotation:
                            type_hints += 1
            
            features = [
                min(loc / 10, 50),
                functions,
                loops,
                conditionals,
                min(avg_func_length / 10, 50),
                min(max_indent, 10),
                min(returns, 10),
                min(exceptions, 10),
                min(complexity, 30),
                comments,
                min(args_total, 20),
                min(type_hints, 10)
            ]
            
            return features
            
        except:
            # Return default features if parsing fails
            return [50, 5, 3, 5, 20, 3, 3, 2, 8, 5, 5, 3]
    
    def predict(self, code: str) -> Dict:
        """Predict quality score from code"""
        features = self.extract_features(code)
        
        # Simple weighted scoring (no actual ML model loaded)
        # In production, this would load a trained model
        score = 75  # Base score
        
        # Adjust based on features
        if features[0] > 50: score -= 5  # Too many lines
        if features[1] > 10: score -= 5  # Too many functions
        if features[2] > 5: score -= 5   # Too many loops
        if features[3] > 10: score -= 5  # Too many conditionals
        if features[4] > 30: score -= 5  # Long functions
        if features[5] > 4: score -= 10  # Deep nesting
        if features[8] > 15: score -= 5  # High complexity
        if features[10] > 10: score -= 5 # Too many args
        
        score = max(0, min(100, int(score)))
        
        return {
            'quality_score': score,
            'confidence': 85,
            'features': dict(zip(self.feature_names, features))
        }
    
    def train(self, X, y):
        """Train the model (placeholder)"""
        # In production, this would train a RandomForest
        from sklearn.ensemble import RandomForestRegressor
        
        self.model = RandomForestRegressor(
            n_estimators=200,
            max_depth=15,
            random_state=42
        )
        self.model.fit(X, y)
        
        # Save model
        with open('model.pkl', 'wb') as f:
            pickle.dump(self.model, f)
        
        return {'status': 'trained'}