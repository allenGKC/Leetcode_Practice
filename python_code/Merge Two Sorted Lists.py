'''
Problem:Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        '''
        非递归
        '''
        p = l1
        q = l2
        cur = tmp =  ListNode(0)
        while p and q :
            if p.val<q.val:
                cur.next = p
                p = p.next
            else:
                cur.next = q
                q = q.next
            cur = cur.next
        '''
        while p:
            cur.next = p
            p = p.next
            cur = cur.next
        while q:
            cur.next = q
            q = q.next
            cur = cur.next
        '''
        cur.next = p or q
        return tmp.next
    '''
    other methods
    递归
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2

    '''   
'''
Test Case:
'''
if __name__ == '__main__':
    