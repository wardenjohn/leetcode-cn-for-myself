class Solution:
    def reverseString(self, s: 'List[str]') -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tail = len(s) - 1
        for i in range(len(s)//2):
            tmp = s[i]
            s[i] = s[tail]
            s[tail] = tmp
            tail -= 1
        print(s)