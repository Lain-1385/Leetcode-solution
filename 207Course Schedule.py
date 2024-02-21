class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites == []:
            return True
        mydict = {}
        myset = set()
        for i in prerequisites:
            mydict[i[0]]= i[1]
        
        cur_class = prerequisites[0][0]
        while mydict:
            if cur_class in mydict:
                temp = mydict[cur_class]
                mydict.pop(cur_class)
                if temp in myset or temp == cur_class:
                    return False
                else:
                    myset.add(cur_class)
                cur_class = temp
            else:
                myset.clear()
                cur_class = next(iter(mydict.items()))[0]
        return True
            
 