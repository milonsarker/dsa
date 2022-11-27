#https://leetcode.com/problems/remove-linked-list-elements/?envType=study-plan&id=data-structure-i

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ptr = head
        prev = None
        while ptr:
            if ptr.val == val:
                if prev is None:
                    head = ptr.next
                else:
                    prev.next = ptr.next
                ptr = ptr.next
            else:
                prev = ptr
                ptr = ptr.next
        return head
