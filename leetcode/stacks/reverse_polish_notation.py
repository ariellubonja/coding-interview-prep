class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            try:
                token = int(token)
                stack.append(token)
            except ValueError:
                if token == "+":
                    res = stack.pop() + stack.pop()
                elif token == "-":
                    second_op = stack.pop()
                    first_op = stack.pop()
                    res = first_op - second_op
                elif token == "*":
                    res = stack.pop() * stack.pop()
                elif token == "/":
                    second_op = stack.pop()
                    first_op = stack.pop()
                    res = int(first_op / second_op)
                
                stack.append(res)
            
        return stack[-1]
            
