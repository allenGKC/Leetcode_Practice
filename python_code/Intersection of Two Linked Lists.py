'''
Problem:Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.

Notes:

1.If the two linked lists have no intersection at all, return null.
2.The linked lists must retain their original structure after the function returns.
3.You may assume there are no cycles anywhere in the entire linked structure.
4.Your code should preferably run in O(n) time and use only O(1) memory.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p,q = headA,headB
        lengthA,lengthB = 0,0
        if p is None or q is None:
            return None
        while p and p.next:
            p = p.next
            lengthA +=1
        while q and q.next:
            q = q.next
            lengthB +=1
        if p != q:
            return None
        else:
            p,q = headA,headB
            if lengthA>lengthB:
               for i in range(lengthA-lengthB):
                   p = p.next
            else:
               for i in range(lengthB-lengthA):
                   q = q.next
            while p!=q:
                p = p.next
                q = q.next
            return q
               
        
'''
Test Case:
'''
if __name__ == '__main__':
    