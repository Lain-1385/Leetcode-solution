'''
# failed
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res = []
        #dict_index = defaultdict()
        dict = {}
        for index in range(0, len(accounts)):
            repeat = False
            num_del = 0
            for i in range(1, len(accounts[index])):
                if accounts[index][i - num_del] not in dict:
                    dict[accounts[index][i - num_del]] = index
                else:
                    repeat == True
                    name_index = dict[accounts[index][i - num_del]]
                    del accounts[index][i - num_del]
                    num_del += 1
                    #dict_index[index] = name_index
            if repeat == True:
                res[name_index].append(accounts[index][1:])
            else:
                res.append(accounts[index])
            
        for account in res:
            account = account[0] + sorted(account[1:])
        return res
'''            
# solution DFS 
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        em_to_name = {}
        graph = defaultdict(set)
        # construct a graph, in which the node is email. Each email in the account is connected to the first email.(including itself)
        # in this graph, connected nodes are considered to belong one user.
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                # when email is already in graph, it makes two blocks connected
                graph[email].add(acc[1])
                em_to_name[email] = name
        seen = set()
        ans = []
        # traverse graph
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    # use component too record all connected nodes.
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans
#Disjoint Set Union
class Solution:
    def accountsMerge(self, accounts):
        parent = {}
        em_to_name = {}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(y)] = find(x)

        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                if email not in parent:
                    parent[email] = email
                em_to_name[email] = name
                union(acc[1], email)

        trees = collections.defaultdict(list)
        for email in parent.keys():
            trees[find(email)].append(email)

        return [[em_to_name[root]] + sorted(emails) for root, emails in trees.items()]