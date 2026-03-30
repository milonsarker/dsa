#https://leetcode.com/problems/binary-tree-level-order-traversal/description/?envType=study-plan&id=level-1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if not root:
            return answer
        def traverse(node, level):
            if len(answer) == level:
                answer.append([])
            answer[level].append(node.val)
            if node.left:
                traverse(node.left, level + 1)
            if node.right:
                traverse(node.right, level + 1)
        traverse(root, 0)
        return answer