class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif char == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif char == '}':
                if not stack or stack.pop() != '{':
                    return False
        if stack == []:
            return True
        else:
            return False