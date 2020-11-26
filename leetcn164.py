class Solution:
    def maximumGap(self, nums: list) -> int:
        if len(nums) < 2:
            return 0

        nums.sort()
        max_gap = 0
        for i in range(0, len(nums)-1):
            if nums[i+1] - nums[i] > max_gap:
                max_gap = nums[i+1] - nums[i]
        return max_gap

a = Solution()
a.maximumGap([3,6,9,1])