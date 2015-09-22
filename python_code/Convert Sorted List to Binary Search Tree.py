'''
Problem:Convert Sorted List to Binary Search Tree
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        num = []
        p = head
        while p:
            num.append(p.val)
            p = p.next
        return self.sortedArrayToBST(num)
        
    
    def sortedArrayToBST(self,num):
        if not num:
            return None
        mid = len(num)/2
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])
        return root
        
'''
Test Case:
'''
if __name__ == '__main__':
    