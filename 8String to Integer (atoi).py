class Solution:
    def myAtoi(self, s: str) -> int:
        target_str = []
        for i in s:
            if not target_str and i == ' ':
                continue
            elif not target_str and (i == '-' or i == '+'):
                target_str.append(i)
                continue
            elif i > '9' or i < '0':
                break
            target_str.append(i)
        if not target_str:
            return 0
        flag_positive = 1 # positive
        
        if target_str[0] == "-":
            flag_positive = -1
            target_str.pop(0)
        elif target_str[0] == '+':
            target_str.pop(0)

        res = 0
        for i in target_str:
            res = res * 10 + int(i)
        res = flag_positive * res
        if res < -2147483648:
            return -2147483648
        if res > 2147483647:
            return 2147483647
        return res

#better
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # remove leading whitespaces
        if not s:
            return 0

        # check the sign
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1

        res = 0
        for ch in s:
            if not ch.isdigit():
                break
            res = res * 10 + int(ch)
            if res > 2147483647:
                return 2147483647 if sign == 1 else -2147483648
        return sign * res
    
# C++, emphasize on type(res)
class Solution {
public:
    int myAtoi(string s) {
        int i = 0, sign = 1, res = 0;
        while (s[i] == ' ') { i++; }
        if (s[i] == '-' || s[i] == '+') {
            sign = (s[i++] == '-') ? -1 : 1;
        }
        while (isdigit(s[i])) {
            if (res > INT_MAX / 10 || (res == INT_MAX / 10 && s[i] - '0' > 7)) {
                return (sign == 1) ? INT_MAX : INT_MIN;
            }
            res = res * 10 + (s[i++] - '0');
        }
        return sign * res;
    }
};