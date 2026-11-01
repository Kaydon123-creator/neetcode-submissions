class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def encode(word):
            encode_list = [0]*26
            for c in word:
                encode_list[ord(c)%26] +=1 
            return tuple(encode_list)
            
        result = defaultdict(list)
        for word in strs:
            result[encode(word)].append(word)
        
        return [result[key] for key in result]

        