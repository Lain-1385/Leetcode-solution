class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        # pivot 0 , 0 ,mid ,last
        # pivot is in the first half, order: mid ,last, 0
        # pivot second half, order: last, 0, mid