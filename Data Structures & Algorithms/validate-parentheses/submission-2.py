class Solution:
    def isValid(self, s: str) -> bool:
        stk = deque()

        for c in s:
            if c == '{' or c == '[' or c == '(':
                stk.append(c)
            elif len(stk) == 0:
                return False
            elif c == '}':
                if stk.pop() != '{':
                    return False
            elif c == ']':
                if stk.pop() != '[':
                    return False
            elif c == ')':
                if stk.pop() != '(':
                    return False
        return len(stk) == 0