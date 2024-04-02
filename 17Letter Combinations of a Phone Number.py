class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        num2str = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], 
                   '6': ['m', 'n', 'o'], '7':['p','q','r','s'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        res = []
        def backtrack(path, digits: str):
            if len(digits) == 0:
                # path is reference(mutable) and path[:] is shallow copy
                
                res.append(path[:])
                return None
            for i in num2str[digits[0]]:
                path += i
                backtrack(path, digits[1:])
                path = path[:-1]
        path = ""
        backtrack(path, digits)
        return res