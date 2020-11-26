# not AC
class Solution:
    def combinationSum3(self, k: int, n: int):
        ans = []
        for i in range(9, -1, -1):
            ans.append(self.search_ans(k, n, [], i))
        output = []
        for each in ans:
            if each is None:
                pass
            else:
                output.append(each)
        return output

    def search_ans(self, left, remind_total, combine_list:list, start):
        if start == 0:
            return None
        if start > remind_total:
            return None
        else:
            if remind_total == 0 and left == 0:
                return combine_list
            else:
                if start < remind_total:
                    combine_list.append(start)
                    left -= 1
                    remind_total -=start
                    return self.search_ans(left, remind_total, combine_list, start-1)
                else:
                    return self.search_ans(left, remind_total, combine_list, start-1)


a = Solution()
print(a.combinationSum3(3, 7))