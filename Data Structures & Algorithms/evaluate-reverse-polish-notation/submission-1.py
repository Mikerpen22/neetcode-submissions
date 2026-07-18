from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = deque()
        operators = ['+', '-', '*', '/']
        
        for tok in tokens:
            if tok not in operators:
                stk.append(tok)
                continue
            else:
                right = int(stk.pop())
                left = int(stk.pop())
                if tok == '+':
                    stk.append(str(left + right))
                elif tok == '-':
                    stk.append(str(left - right))
                elif tok == '*':
                    stk.append(str(left * right))
                else:
                    stk.append(str(int(left / right)))
        
        return int(stk[-1])
