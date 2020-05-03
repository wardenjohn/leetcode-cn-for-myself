"""
快乐数就是要考虑三个情况，1：就是最终就是1
2：回到循环
3：趋近无穷大
分析，对于4位数以上的最大数9999 or bigger
每一次计算都会掉一位，知道掉到3位数为止
所以第三种情况不用考虑
那就看看有没有循环，有循环了就是false，否则就是true
"""
class Solution:
    def isHappy(self, n: 'int') -> 'bool':

        def getNextNum(n):
            totalSum = 0
            while n > 0:
                n, digt = divmod(n, 10)
                totalSum += digt ** 2
            return totalSum

        sets = set()
        
        while n != 1 and n not in sets:
            sets.add(n)
            n = getNextNum(n)
        
        if n == 1:
            return True
        else:
            return False

sol = Solution()
print(sol.isHappy(19))