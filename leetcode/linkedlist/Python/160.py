#https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        addrs_dict = {}
        while headA or headB:
            if headA:
                if headA not in addrs_dict:
                    addrs_dict[headA] = 1
                    headA  = headA.next
                else:
                    return headA
            if headB:
                if headB not in addrs_dict:
                    addrs_dict[headB] = 1
                    headB = headB.next
                else:
                    return headB