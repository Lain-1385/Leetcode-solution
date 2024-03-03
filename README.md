# Leetcode-solution
## 150 stack easy
in python, "//" means the floor and int() means discard decimal part.

## 1 hash easy
dictionary is a data structure implemented based on a hash table.

## 15 hash medium O(n^2)
Enumerating the element a in list, this problem becomes a sub-question: to find b+c = -a.
output is required and to be ordered, so we need to order input list at first.
tips: set() is an unordered collection of unique elements.

## 100 binary_tree easy O(min(n,m)) 
recursive solution, the key si to analyze the situations in which p or q is None.
'self' is a reference to the object itself. 'self' represents the instance of the class on which the method is called. We need to use self.isSameTree() instead of isSameTree() because it's a instant method within the 'Solution' class.
p: Optional[Treenode] is a part of python type hint, p is name; Optional means p can be Treenode or None.
--> bool: is a part of type hint, it means this function returns bool value.

## 151 str medium O(n)
Very easy if using library function
my solution is using stack to reverse
another solution: two pointers. 1. remove extra spaces 2. reverse the whole str 3.reverse each word in str

## 11 greedy medium O(n)
use two pointer to get water volumn. local optimal solution is to move the short side to taller position. Iterate the whole list to get global optimal solution.

## 45 dp medium O(n)
employ the proof by contradiction to prove dp[i] <= dp[i + 1],then get dp[i] = dp[j] + 1(j is the first which can jump to i)
dp is not the same as recursion, dp usually use a table or something to restore sub-question solution information to avoid repeated calculation.

## 50 divide medium O(logn)
divide into two situation n = odd or even, need to set n = -1 as an exit when n < 0.

## 70 dp easy O(n)
in fact, this is a Fibonacci sequence.

## 121 array easy O(n)
Too easy to explain anything.

## 21 Listnode easy O(n)
Classic.should recite.

## 125 string easy O(n)
Too easy. The code would be short if we use regular expression and python reverse function.

## 226 binaryTree easy O(n)
Classic.should recite.

## 242 dict easy O(n)
Use hash table like dict or set when position information is not crucial.

## 704 binarysearch/two pointers easy O(n)
Classic, recite.

## 733 recursion easy O(n)
Easy.

## 235 BST medium O(logn)
if two nodes are both smaller than root, search root's left.
if two nodes are both bigger than root, search root's right.
otherwise, return root. 

## 110 Tree easy O(n)
when node is unbalanced, let depth be -1, and stop in advance when left tree or right become unbalanced.
in this case we just need one time traverse.

## 232 stack easy O(n)
divide two stacks into input and output, and only output become empty we need to pour all element of input stack into output stack.

## 278 BinarySearch easy O(n)
classical, two solution and be care about < or <=, mid or mid + 1 , return mid or left

## 383 string easy O(n)
if an abnormal situation occurs during the process, should output False

## 409 string easy o(n)
dont need to iterate set or dict again.

## 169 array easy O(n)
Sorting, hash map, Moore Voting.
Moore Voting: The algorithm works on the basis of the assumption that the majority element occurs more than n/2 times in the array.This assumption guarantees that even if the count is reset to 0 by other elements, the majority element will eventually regain the lead.

## 67 binary easy O(n)
carry = (a + b + carry) // 2, c = (a + b + carry) % 2

## 543 binary easy O(n)
integer is immutable, so u cant change its value in depth()
Array is mutable, so u can change its value in depth()
u can also use self. to record in the process of recursion.

## 104 binary easy O(n)
classic

## 876 ListNode easy O(n)
classic

## 217 array easy O(n)
use set.

## 13 string easy O(n)
using hash table and iterate s, judge s[i] and s[i+1], add value or subtract value.

## 844 string easy O(n)
stack.pop() when iterating '#', return stack.t == stack.s

## 53 array medium O(n)
DP: construct a subproblem -- find the maximum subsequence sum ending with the Nth element. e.g. for [-2,1,-3]
s[1] = -2 s[2] = 1 s[3] = -2, we can find s[n+1] = max(s[n], 0) + nums[n]. then global result is max[s].

greedy: use a current_sum to record local_maximum, when it becomes negative, it needs to inial as 0. use res to output the max current_sum.

## 57 array medium O(n)
very complex, split it into 4 subquestion. see note in my code.

## 542 dp medium O(mn)
brush tiles twice. First, compute distance towards left and up. Second, compute distance towards right and down.

## 973 array medium O(nlogk)
logic is simple, we can use heap to make code more clear.

## 3 hash medium O(n)
use dict, add char and index into dict, when char is already in dict(meet repeated char), compute the index subtraction. return the max subtraction.

## 102 BT medium O(n)
queue implement BFS, record each node's level. when level updates, the res_array should add a new subarray. when level remains unchanged, only the last subarray in res updates.

## 207 topological sort medium O(n)
defaultdict(list) is very useful, it can automatically add values into a value-list when key can be repeated.
we use a indegree list to record each course's in-degree. For those whose indegree equals 0(need no pre-course), we add them into a queue to implement BFS. when we iterate a course, we should decrese its post-course by 1 and check its in-degree , append it into queue or not.
DFS: use a list containing three state: -1 visiting 0 unvisited 1 visited, if meets -1, it indicates a loop is found.

## 207 Trie medium
Trie structure. The node is nested dictionary, the key is char and the value is {}. the end of the Trie should be marked, like use {'*'} as key. 

## 238 array medium O(n)
use prefix product and suffix product, the i-th target outpush should be prefix[i] * suffix[i]

## 155 stack medium O(1)
use a list to record the current min_value when execute pushing.

## 98 BST medium O(n)
use validate(node, min_val, max_val), update min_val, max_val in each iterations.

## 200 dfs medium O(mn)
use a dfs function to convert all island connected to given point to water, call this funtion and count num_island in outer iterative when met with island.

## 994 bfs medium O(mn)
use BFS, append all rotten orange position into queue to initialize it.