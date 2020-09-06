# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 执行用时：44 ms, 在所有 Python3 提交中击败了64.23%的用户
# 内存消耗：13.8 MB, 在所有 Python3 提交中击败了94.09%的用户
class Solution:
    def levelOrderBottom(self, root: TreeNode):
        levels = []
        wait_read_list = []
        wait_read_list.append(root)
        this_level = 1
        this_level_bef = 1
        this_level_list = []
        for each_node in wait_read_list:
            if each_node is None:
                wait_read_list.pop(0)
            else:
                if this_level > 0:
                    this_level_list.append(each_node.val)
                    if each_node.left is not None:
                        wait_read_list.append(each_node.left)
                    if each_node.right is not None:
                        wait_read_list.append(each_node.right)
                    this_level -= 1
                if this_level == 0:
                    levels.append(this_level_list)
                    this_level_list = list()
                    this_level = len(wait_read_list) - this_level_bef
                    this_level_bef = len(wait_read_list)
        levels.reverse()
        return levels