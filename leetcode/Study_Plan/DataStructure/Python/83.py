#https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/?envType=study-plan&id=data-structure-i

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        ptr = head
        while ptr:
            if prev is not None and prev.val == ptr.val:
                prev.next = ptr.next
                ptr = ptr.next
            else:
                prev = ptr
                ptr = ptr.next
        return head