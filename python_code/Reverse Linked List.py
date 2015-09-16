'''
Problem:Reverse Linked List
Reverse a singly linked list.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        p1 = head
        p2 = p1.next
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        head.next = None
        head = p1
        return head

'''
Test Case:
'''
if __name__ == '__main__':
    