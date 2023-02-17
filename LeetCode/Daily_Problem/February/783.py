#https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        minimum = 10 ** 5
        min2nd = 10 ** 5
        vals = []
        stack = [root]
        while stack:
            vNode = stack.pop()
            if vNode.left:
                stack.append(vNode.left)
            if vNode.right:
                stack.append(vNode.right)
            vals.append(vNode.val)
        vals.sort()
        for i in range(1, len(vals)):
            if minimum > vals[i] - vals[i - 1]:
                minimum = vals[i] - vals[i - 1]
        return minimum
