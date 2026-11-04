class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        length = n + m 
        i = 0 
        j = 0 
        curr = prev = -1
        while (i+j) <= (length // 2):
            prev = curr

            if i < n and (j >= m or nums1[i] < nums2[j]):
                curr = nums1[i]
                i+=1 
            else:
                curr = nums2[j]
                j+=1
                
        if length%2 == 0:
            return (prev+curr)/2 
        else:
            return curr
            
            
        
