class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def ordered_nums(nums: List[int]):
            res = [1]
            cur = 1
            for i in nums:
                cur = cur * i
                res.append(cur)
            return res
        
        def reversed_nums(nums: List[int]):
            res = [1] * len(nums)
            cur = 1
            for i in range(len(nums), 0, -1):
                cur = cur * nums[i]
                res[i - 1] = cur
            return res
        ordered_list = ordered_nums(nums)
        reversed_list = reversed_nums(nums)
        res = []
        for i in range(len(nums)):
            res.append(reversed_list[i] * ordered_list[i])
        return res
    

# O(1)     
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0]*length

        # answer[i] contains the product of all the numbers to the left of i
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]

        # Now for each i, calculate product of all the numbers to the right
        # and multiply it with the product of numbers to the left
        R = 1;
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer