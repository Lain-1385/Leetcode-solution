class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        str_len = len(s)
        res = 0
        myset = set()
        right = 0
        for left in range(str_len):
            if left > 0:
                myset.remove(s[left - 1])
            while(s[right] not in myset):
                if right == str_len - 1:
                    return res if right - left + 1 < res else right - left + 1
                myset.add(s[right])
                right += 1
            res = max(res, right - left)
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_len = len(s)
        res = 0
        mydict = {}
        left = 0
        for right in range(str_len):
            if s[right] in mydict:
                left = max(mydict[s[right]] + 1, left)
            mydict[s[right]] = right
            res = max(res, right - left + 1)
        return res


s = "pwwkew"
a = Solution()
print(a.lengthOfLongestSubstring(s))