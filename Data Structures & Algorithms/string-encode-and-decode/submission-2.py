class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result+= str(len(word))+"#"+word
        return result

    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0 
        result = []
        while i < n :
            j = i 
            ans = ""
            length = ""
            while j < n and s[j] != "#":
                length+= s[j]
                j+=1 
            print(length, j, i)
            length = int(length)
            for k in range(j+1, j+1 + length):
                ans+=s[k]
            result.append(ans)
            i = j+1 + length
        return result 



        