class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range (len(s)):
            if s[i] == "[":
                stack.append("]")
                continue
            if s[i] == "(":
                stack.append(")")
                continue
            if s[i] == "{":
                stack.append("}")
                continue
            if len(stack) > 0 and s[i] == stack[-1]:
                stack.pop()
                continue
            return False
        return len(stack) == 0
            

        