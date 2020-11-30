#二叉树的层序遍历
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: 'TreeNode') -> List[List[int]]:
        nodes = []
        self.searchNodes(root, nodes, 0)
        return nodes

    def searchNodes(self, root:'TreeNode', nodes, level):
        #level means this level
        if root is not None:
            if len(nodes) <= level:
                thisLevel = []
                thisLevel.append(root.val)
                nodes.append(thisLevel)
                self.searchNodes(root.left, nodes, level+1)
                self.searchNodes(root.right, nodes, level+1)
            else:
                nodes[level].append(root.val)
                self.searchNodes(root.left, nodes, level+1)
                self.searchNodes(root.right, nodes, level+1)
        return nodes
