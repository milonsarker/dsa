#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        curLevel = [root]
        nextLevel = []
        flag = 1
        result = []
        curVal = []
        if root == None:
            return []
        while curLevel:
            node = curLevel.pop()
            curVal.append(node.val)
            if flag == 0:
                if node.right:
                    nextLevel.append(node.right)
                if node.left:
                    nextLevel.append(node.left)
            else:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if len(curLevel) == 0:
                curLevel = nextLevel
                nextLevel = []
                result.append(curVal)
                curVal = []
                flag = 0 if flag == 1 else 1
        return result