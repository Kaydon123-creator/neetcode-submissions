class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        digit_map = {
           "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"
        }
        n = len(digits)
        result = []
        #d -> which digit, i -> which letter
        def backtrack(d, path):
            if len(path)==len(digits):
                result.append("".join(path))
                return 
            letters = digit_map[digits[d]]
            for i in range(len(letters)):
                path.append(letters[i])
                backtrack(d+1,path)
                path.pop()
        backtrack(0,[])
        return result
            

        
        