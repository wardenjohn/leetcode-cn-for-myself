class Solution:
    def reverseWords(self, s: 'str') -> str:
        lists = s.split(' ')
        string = ""
        # print(len(lists))
        for count in range(len(lists)):
            # print(lists[count])
            if count == len(lists) - 1:
                string+=''.join(reversed(lists[count]))
            else:
                string+=''.join(reversed(lists[count]))
                string+=" "
        return string