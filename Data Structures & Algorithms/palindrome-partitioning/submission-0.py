class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            for i in range(len(s)//2):
                if s[i]!=s[len(s)-1-i]:
                    return False
            return True
    
        result = []
        def backtrack(index,path):
            if index >= len(s) :
                result.append(path[::])
                return
             
            for i in range(index, len(s)):
                if isPalindrome(s[index:i+1]):
                    path.append(s[index:i+1])
                    backtrack(i+1, path)
                    path.pop()
        backtrack(0, [])
        return result
                
            
        

        