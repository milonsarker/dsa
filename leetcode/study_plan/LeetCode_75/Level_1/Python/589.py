#https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        print(root)
        if root == None:
            return []
        stack = [root]
        output = []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
        return output