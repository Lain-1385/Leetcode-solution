class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for i in s:
            if i != '#':
               stack_s.append(i)
            elif stack_s:
               stack_s.pop()
        for i in t:
            if i != '#':
               stack_t.append(i)
            elif stack_t:
               stack_t.pop()
        return stack_s == stack_t


