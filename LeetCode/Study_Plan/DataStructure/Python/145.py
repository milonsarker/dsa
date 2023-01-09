#https://leetcode.com/problems/binary-tree-postorder-traversal/description/?envType=study-plan&id=data-structure-i

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        answer = []
        visited = {}
        if not root:
            return []
        while stack:
            node = stack.pop()
            if node not in visited:
                stack.append(node)
                visited[node] = 1
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            else:
                answer.append(node.val)
        return answer