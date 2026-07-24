from client import AiVibeCoderRefactoringEngineClient

def main():
    client = AiVibeCoderRefactoringEngineClient()
    res = client.refactor_vibe("Make this function super clean and bulletproof", "def process(x): return x * 2")
    print("Improvements Applied:")
    for imp in res["improvements"]:
        print(f"  - {imp}")
    print("Optimized Code:")
    print(res["optimized_code"])

if __name__ == "__main__":
    main()
