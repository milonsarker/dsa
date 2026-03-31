#https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        data = []
        while head:
            data.append(head.val)
            head = head.next
        i = 0
        j = len(data) - 1
        while j >= i:
            if data[i] != data[j]:
                return False
            else:
                j -= 1
                i += 1
        return True