class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        for i in range(len(s) - 1):
            current_value = dict[s[i]]
            if current_value < dict[s[i + 1]]:
                res -= current_value
            else:
                res += current_value
        res += dict[s[len(s) - 1]]
        return res