class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        set = {}
        for i in ransomNote:
            if i in set:
                set[i] += 1
            else:
                set[i] = 1
        for i in magazine:
            if i in set:
                set[i] -= 1
        
        for _,val in set.items():
            if val > 0:
                return False
        return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i, "", 1)
            else:
                return False
        return True
        