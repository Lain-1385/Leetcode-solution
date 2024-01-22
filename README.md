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