#https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        start = head
        while start:
            for i in range(m):
                if start.next:
                    previous = start
                    start = start.next
                else:
                    return head
            for i in range(n):
                if start.next == None:
                    previous.next = None
                    return head
                elif start.next:
                    start= start.next
                    previous.next = start

