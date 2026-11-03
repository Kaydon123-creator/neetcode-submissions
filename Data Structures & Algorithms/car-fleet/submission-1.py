class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    
        import math 

        speed_map = {}

        for i in range(len(position)):
            speed_map[position[i]] = speed[i]

        position.sort()
        stack = []

        for i in range(len(position)):
            while stack and (target- position[i])/speed_map[position[i]]>=stack[-1]:
                stack.pop()
            stack.append((target- position[i])/speed_map[position[i]])
        return len(stack)

        



