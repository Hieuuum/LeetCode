# 150. Evaluate Reverse Polish Notation (Medium)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Hint 3
        # Compiled to Debug

        stack = []

        for cur in tokens:
            if cur == "+":
                stack.append(stack.pop() + stack.pop())
            elif cur == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif cur == "*":
                stack.append(stack.pop() * stack.pop())
            elif cur == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else: 
                stack.append(int(cur))
        
        return stack[0]