class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_str = {}
        for i in s:
            if i in dict_str:
                dict_str[i] += 1
            else:
                dict_str[i] = 1
        for i in t:
            if i in dict_str:
                dict_str[i] -= 1
            else:
                return False
        
        for _, val in dict_str.items():
            if val != 0:
                return False
        return True

a = Solution()
print(a.isAnagram("a","a"))
