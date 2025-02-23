from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current: str, open_count: int, close_count: int):
            # Base case: If the current string has 2n characters, add it to the result
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Add an opening parenthesis if we haven't used all n
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            # Add a closing parenthesis if it does not exceed open_count
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        
        # Start the recursion
        backtrack("", 0, 0)
        return result
