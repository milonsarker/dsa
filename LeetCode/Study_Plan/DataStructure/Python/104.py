#https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan&id=data-structure-i

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        levels = []
        depth = 0
        if not root:
            return 0

        def traverse(node, level):
            if len(levels) == level:
                levels.append([])
            if node.left:
                traverse(node.left, level + 1)
            if node.right:
                traverse(node.right, level + 1)

        traverse(root, 0)
        return len(levels)
