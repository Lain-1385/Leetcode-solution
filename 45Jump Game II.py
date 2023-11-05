class Solution:
    def jump(self, nums: List[int]) -> int:
        # TODO:optimal solution as it exceed limitted time when facing a long list nums
        if len(nums) == 1:
           return 0
           

        for i in range(len(nums) - 1):
           if i + nums[i] >= len(nums) - 1:
               return self.jump(nums[:i + 1]) + 1