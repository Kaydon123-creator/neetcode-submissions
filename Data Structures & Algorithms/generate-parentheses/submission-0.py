class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(stack, open, close):
            if open ==close == n :
                result.append("".join(stack))
            if open < n :
                stack.append("(")
                backtrack(stack, open+1, close)
                stack.pop()
            if close < open:
                stack.append(")")
                backtrack(stack, open, close+1)
                stack.pop()
        backtrack([], 0, 0)
        return result
            