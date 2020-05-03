# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        val = []
        node = l1
        while node is not None:
            val.append(node.val)
            node = node.next
        node = l2
        while node is not None:
            val.append(node.val)
            node = node.next
        val.sort()
        if len(val) == 0:
            return None

        head = ListNode()
        pre = head
        
        for i in range(len(val)):
            if i == 0:
                pre.val = val[i]
            else:
                now = ListNode()
                now.val = val[i]
                pre.next = now
                pre = now
        return head


