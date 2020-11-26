class Solution:
    def runningSum(self, nums: list) -> list:
        for i in range(0, len(nums)):
            if i == 0:
                pass
            else:
                nums[i] = nums[i] + nums[i-1]
        return nums
