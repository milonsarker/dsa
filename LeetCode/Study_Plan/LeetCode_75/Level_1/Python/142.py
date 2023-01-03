#https://leetcode.com/problems/linked-list-cycle-ii/description/?envType=study-plan&id=level-1


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        add_list = {}
        while head:
            if head not in add_list:
                add_list[head] = 1
                head = head.next
            else:
                return head
        return head