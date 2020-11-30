"""
最大子序和
扫描法O(N)：当我们加上一个正数时，和会增加；当我们加上一个负数时，和会减少。如果当前得到的和是个负数，那么这个和在接下来的累加中应该抛弃并重新清零，不然的话这个负数将会减少接下来的和。
下面这个是动态规划：O(N)
"""
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> int:
        sum_l = nums[0]
        n = nums[0]

        for i in range(1,len(nums)):
            if n > 0:
                n += nums[i]
            else:
                n = nums[i]
            if sum_l < n:
                sum_l = n
        return sum_l

"""
class Saomiao:
    def maxSubArray(self, nums: 'List[int]') -> int:
        int current=nums[0];
        int sum=nums[0];
        //我们考虑如果全是负数，那么返回最大的负数，如果最后的和为正，那么就使用扫描法
        for(int i=1;i<nums.length;i++) {
            if(current<0)current=nums[i];#当前数小于0 肯定会舍去（否则将会影响接下来的和），换为下一个数
            else current+=nums[i];#如果当前数不小于0，那么他会对接下来的和有积极影响
            if(current>sum)sum=current;#这里既实现了负数返回最大也实现了扫描法
            #这里其实已经隐式的列举了所有可能，保留了所有可能的最大值
        }
"""