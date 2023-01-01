#https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        rem_val = 0
        start = ListNode()
        return_list = start
        previous = start
        first = l1
        second = l2
        while first or second or rem_val > 0:
            if return_list == None:
                new_node = ListNode()
                return_list = new_node
                previous.next  = return_list
                previous = return_list
            if first and second:
                return_list.val = (first.val + second.val + rem_val) % 10
                rem_val = (first.val + second.val + rem_val) // 10 if (first.val + second.val + rem_val) >= 10 else 0
                first = first.next
                second = second.next
                return_list = return_list.next
            elif first:
                return_list.val = (first.val + rem_val) % 10
                rem_val = (first.val +  rem_val) // 10  if (first.val + rem_val) >= 10 else 0
                first = first.next
                return_list = return_list.next
            elif second:
                return_list.val = (second.val + rem_val) % 10
                rem_val = (second.val +  rem_val) // 10 if (second.val + rem_val) >= 10 else 0
                second = second.next
                return_list = return_list.next
            else:
                return_list.val = rem_val
                rem_val = 0
        return start