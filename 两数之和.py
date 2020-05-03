"""
这个题的想法是直接就是暴力解法，但是效率比较低下咯
"""
class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int'):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    tmp = []
                    tmp.append(i)
                    tmp.append(j)
                    return tmp

sol = Solution()
nums = [2,7,11,15]
target = 9
print(sol.twoSum(nums, target))