class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        result.append(intervals[0])
        end = result[0][1]

        for inter in intervals[1:]:
            if inter[0] <= end:
                new_end = max(inter[1], result[-1][1])
                result[-1][1] = new_end
                
            else:
                result.append(inter)
            end = result[-1][1]
        return result

            
        