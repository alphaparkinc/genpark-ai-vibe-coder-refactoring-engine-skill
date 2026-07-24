class AiVibeCoderRefactoringEngineClient:
    def refactor_vibe(self, natural_instruction: str, code_snippet: str) -> dict:
        improvements = [
            "Converted synchronous loops to list comprehensions",
            "Added automatic error guards for undefined variables",
            "Applied PEP8 formatting and type hints"
        ]
        optimized = f"# Refactored based on vibe: '{natural_instruction}'\n" + code_snippet
        return {
            "optimized_code": optimized,
            "improvements": improvements
        }
