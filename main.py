import re
import ast
from typing import List
from transformers import pipeline

class CodeReviewer:
    def __init__(self):
        self.linter = pipeline("text2text-generation", model="facebook/bart-large-cnn")

    def check_naming_conventions(self, code: str) -> List[str]:
        suggestions = []
        variables = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', code)
        for var in variables:
            if not re.match(r'^[a-z_][a-z0-9_]*$', var):
                suggestions.append(f"Variable '{var}' should follow snake_case naming convention.")
        return suggestions
    
    def analyze_code_structure(self, code: str) -> List[str]:
        suggestions = []
        try:
            tree = ast.parse(code)
            function_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            if not function_names:
                suggestions.append("Consider modularizing your code by using functions.")
        except SyntaxError:
            suggestions.append("Syntax error detected. Please check your code syntax.")
        return suggestions
    
    def suggest_code_improvements(self, code: str) -> List[str]:
        summary = self.linter(code, max_length=100, truncation=True)
        return [summary[0]['generated_text']]
    
    def review_code(self, code: str) -> List[str]:
        suggestions = []
        suggestions.extend(self.check_naming_conventions(code))
        suggestions.extend(self.analyze_code_structure(code))
        suggestions.extend(self.suggest_code_improvements(code))
        return suggestions
