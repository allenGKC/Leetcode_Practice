'''
Problem:Remove Nth Node From End of List
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
1.Given n will always be valid.
2.Try to do this in one pass.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        pre = dummy = ListNode(0)
        pre.next = head
        p = head
        q = head
        i = 0
        for i in range(n-1):
            q = q.next
        while q.next:
            pre = p
            p = p.next
            q = q.next
        pre.next = p.next
        return dummy.next
        
'''
Test Case:
'''
if __name__ == '__main__':
    