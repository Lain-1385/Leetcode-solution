class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        c = ""
        temp = 0
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                cal = temp + int(a[i]) + int(b[j])
            elif j < 0:
                cal = temp + int(a[i]) + 0
            elif i < 0:
                cal = temp + 0 + int(b[j])
            temp = cal // 2
            c = str(cal % 2) + c
            i -= 1
            j -= 1
        if temp == 1:
            c = "1" + c
        return c
    

#after copilot simplify
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, carry, res = len(a) - 1, len(b) - 1, 0, []
        while i >= 0 or j >= 0 or carry:
            n1 = int(a[i]) if i >= 0 else 0
            n2 = int(b[j]) if j >= 0 else 0
            carry, curr = divmod(n1 + n2 + carry, 2)
            res.append(str(curr))
            i, j = i - 1, j - 1
        return ''.join(res[::-1])

 