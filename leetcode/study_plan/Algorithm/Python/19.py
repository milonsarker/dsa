#https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=study-plan&id=algorithm-i


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_list = []
        while head:
            node_list.insert(0, head)
            head = head.next
        lenth = len(node_list)
        if lenth == 1:
            return None
        cntr = 0
        for i in range(len(node_list)):
            if i + 1 == n:
                if i + 1 == lenth:
                    return node_list[-2]
                elif i + 1 == 1:
                    node_list[i + 1].next = None
                    return node_list[-1]
                else:
                    node_list[i + 1].next = node_list[i - 1]
                    return node_list[-1]

