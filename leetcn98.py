#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
class Solution:
    def isValidBST(self, root: 'TreeNode') -> bool:
        if root is None:
            return True
        # maxnum = float('inf') minnum = float('-inf')
        return self.search(root, 99999999999, -99999999999)
 
    def search(self, root: 'TreeNode', max_num, min_num):
        if root is None:
            return True

        if root.val <= min_num or root.val >= max_num:
            return False
        
        if not self.search(root.left, root.val, min_num):
            return False
        
        if not self.search(root.right, max_num, root.val):
            return False
        
        return True

