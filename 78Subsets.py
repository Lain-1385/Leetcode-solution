class Solution:
    def subsets(self, nums):
        def backtrack(first = 0, curr = []):
            #it must be curr[:] not curr
            output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        backtrack(0,[])
        return output
# bit manuplation
class Solution:
    def subsets(self, nums):
        n = len(nums)
        output = []

        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output

def subsets(nums):
    n = len(nums)
    subsets = []
    # There are 2^n possible subsets for a set with n elements.
    for i in range(2**n):
        # For each combination (i), form a subset.
        subset = []
        for j in range(n):
            # Check if the j-th bit of i is set. If so, include nums[j].
            if i & (1 << j):
                subset.append(nums[j])
        subsets.append(subset)
    return subsets