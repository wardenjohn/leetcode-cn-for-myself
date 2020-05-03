"""
无重复字符的最长子串
"""
class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        pos = {}
        head = 0
        tail = head
        max_length = 0
        now_length = 0
        for i in range(len(s)):
            if s[i] in pos.keys():
                pos[s[i]] = i
            else:
                pos[s[i]] = i
        min_l = 99999
        max_l = -1
        for each in pos.keys():
            if pos[each] < min_l:
                min_l = pos[each]
            if pos[each] > max_l:
                max_l = pos[each]
        return max_l - min_l
        # while tail < len(s):
        #     if s[tail] in pos.keys():
        #         head = tail
        #         pos.clear()
        #     else:
        #         now_length = tail - head + 1
        #         pos[s[tail]] = tail
        #         if now_length > max_length:
        #             max_length = now_length
        #         tail += 1
        # return max_length

