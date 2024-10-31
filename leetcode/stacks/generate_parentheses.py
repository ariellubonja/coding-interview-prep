class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        def nextParenthesis(string, num_openbrackets, stack, n):
            result = []
            if num_openbrackets == n: # We have all the opens we need
                # Close all and return
                while stack:
                    stack.pop()
                    string += ")"
                
                result.append(string)
            else:
                result.extend(nextParenthesis(string + "(", num_openbrackets+1, stack + ["("], n))
                if stack:
                    result.extend(nextParenthesis(string + ")", num_openbrackets, stack[:-1], n))
                
            return result

        # nextParenthesis(string, num_openbrackets, stack)
        return nextParenthesis("", 0, [], n)
