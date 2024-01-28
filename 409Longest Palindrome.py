class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        odd = 0
        res = 0
        for _,val in dict.items():
            if val % 2 == 0:
                res += val
            else:
                odd = 1
                res += val - 1
        return res + odd


class Solution:
    def longestPalindrome(self, s: str) -> int:
        set_char = set()
        res = 0
        for i in s:
            if i in set_char:
                res += 2
                set_char.remove(i)
            else:
                set_char.add(i)
        return res + (1 if set_char else 0)
