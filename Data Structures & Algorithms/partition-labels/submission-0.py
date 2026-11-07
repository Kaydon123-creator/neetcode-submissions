class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        frequencies = [0]*26

        for char in s :
            frequencies[ord(char)-ord('a')] +=1 

        bucket = set()
        result = []
        l = 0
        print(frequencies)
        for r,c in enumerate(s):
            frequencies[ord(c)-ord('a')]-=1
            bucket.add(ord(c)-ord('a'))

            if all(frequencies[x]==0 for x in bucket):
                print([chr(x+ord('a')) for x in bucket], l)
                result.append(r-l+1)
                l= r + 1
                bucket = set() 
        return result

        