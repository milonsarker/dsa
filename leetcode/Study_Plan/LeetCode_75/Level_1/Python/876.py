#https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=study-plan&id=level-1


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cntr = 0
        llist = []
        while head:
            cntr += 1
            llist.append(head)
            head = head.next
        return llist[(cntr//2)]