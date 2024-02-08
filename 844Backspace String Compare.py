'''class Solution:
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
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        length_s = len(s)
        length_t = len(t)
        i = length_s -1
        j = length_t - 1

        while i >= 0 or j >= 0:
            count_s = count_t = 0
            while (count_s or s[i] == '#') and i >= 0:
                if s[i] == '#':
                    count_s += 1
                else:
                    count_s -= 1
                i -= 1
            temp_1 = s[i] if i >= 0 else None

            while (t[j] == '#' or count_t) and j >= 0:
                if t[j] == '#':
                    count_t += 1
                else:
                    count_t -= 1
                j -= 1
            temp_2 = t[j] if j >= 0 else None

            if j < 0 and temp_1 != None:
                    return False
            if i < 0 and temp_2 != None:
                    return False
            if temp_1 != temp_2:
                return False
            i -= 1
            j -= 1
        return True 