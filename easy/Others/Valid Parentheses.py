class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        len_s = len(s)
        i = 0
        while i < len_s:
            if s[i] == '{' or s[i] == '(' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                elif s[i] == '}' and stack[-1] == '{':
                    stack.pop()
                elif s[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif s[i] == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            i += 1
        if len(stack) != 0:
            return False
        return True
