


#https://leetcode.com/problems/reverse-linked-list/?envType=study-plan&id=data-structure-i


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr_node = head
        while curr_node:
            next_temp = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_temp

        return prev