from typing import List, Any

# ==== DETAILED TEMPLATE ====
class Problem:
    title: str = "printing name using recursion n times"

    description: str = """
use recursion to print name
no testing required here
"""

    # Implement your solution function below:
    @staticmethod
    def user_solution(n:int,name:str) -> Any:
        if n <= 0:
            return
        Problem.user_solution(n-1,name)
        print(name)
        
        
    # Optional reference solution:
    @staticmethod
    def reference_solution(n:int,name:str) -> Any:
        if n <= 0:
                    return
        Problem.reference_solution(n-1,name)
        print(name)

    # TEST CASES
    tests: List[dict] = [
        {"input": (5,"Yash")},
    ]