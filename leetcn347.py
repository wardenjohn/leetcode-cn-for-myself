# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dicto = {}
        for each in nums:
            if each in dicto.keys():
                dicto[each] += 1
            else:
                dicto[each] = 1
        l = sorted(dicto.items(), key=lambda d: d[1])  # 这个是关键点，就是按照字典的值的大小来对key排序
        be = l[-k:]
        be.reverse()
        ans = []
        for i in range(len(be)):
            ans.append(be[i][0])
        return ans