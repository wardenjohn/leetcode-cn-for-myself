# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: 'TreeNode', t: 'TreeNode') -> bool:
        if s is not None and t is not None:
            if s.val != t.val:
                if not self.isSubtree(s.left, t):
                    return self.isSubtree(s.right, t)
                else:
                    return True
            else:
                return self.checkTree(s, t)
        elif t is None:
            return True
        else:
            return False


    def checkTree(self, s:'TreeNode', t:'TreeNode'):
        if s is None and t is None:
            return True

        if s is not None and t is not None:
            if s.val != t.val:
                return False
            else:
                return self.checkTree(s.left, t.left) and self.checkTree(s.right, t.right)
        return False

    #Solution!one sentences ...lol
    # def isSubtree(self, s: 'TreeNode', t: 'TreeNode') -> bool:
    #     return str(s).find(str(t)) != -1