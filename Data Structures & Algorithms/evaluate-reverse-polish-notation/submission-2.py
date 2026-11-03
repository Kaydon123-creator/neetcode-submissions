class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operator = {"+", "-", "/", "*"}
        def parseint(s):
            if t[0] == "-":
                return int(t[1:])*-1
            else:
                return int(t)

        def evaluate(a,b,operator):
   
            match operator:
                case "+":
                    return a+b
                case "-":
                    return a-b
                case "/":
                    
                    return int(a/b)
                case "*":
                    return a*b
                case _:
                    raise ValueError("Invalid value")
        for t in tokens:
            if t in operator:  
                b = stack.pop()
                a = stack.pop()
                stack.append(evaluate(a,b,t))
            else:
                stack.append(parseint(t))
        return stack[0]

                    
                    
                

                
