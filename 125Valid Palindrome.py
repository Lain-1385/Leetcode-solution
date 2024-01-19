class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while not ('a' <= s[i] <='z' or 'A' <= s[i] <='Z' or '0'<= s[i] <= '9') and i < j:
                i += 1
            while not ('a' <= s[j] <='z' or 'A' <= s[j] <='Z' or '0'<= s[j] <= '9') and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

'''
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^A-Za-z0-9]', '', s).lower()
        return s == s[::-1]
'''