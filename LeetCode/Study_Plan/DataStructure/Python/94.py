#https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        answer = []
        visited = {}
        if not root:
            return []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited[node] = 1
                if node.right:
                    stack.append(node.right)
                    stack.append(node)
                else:
                    stack.append(node)
                if node.left:
                    stack.append(node.left)
            else:
                answer.append(node.val)
        return answer