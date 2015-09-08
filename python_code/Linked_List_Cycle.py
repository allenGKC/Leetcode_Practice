'''
Problem:Linked List Cycle 
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        fast = head
        low = head
        while fast and fast.next:
            fast = fast.next.next
            low = low.next
            if fast == low:
                return True
        return False
'''
Test Case:
'''
if __name__ == '__main__':
    