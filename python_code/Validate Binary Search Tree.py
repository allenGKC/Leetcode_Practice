'''
Problem:Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inOrder(self,root,list1):
        if root is None:
            return
        self.inOrder(root.left,list1)
        list1.append(root.val)
        self.inOrder(root.right,list1)
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        l = []
        self.inOrder(root,l)
        
        for i in range(1,len(l)):
            if l[i]<=l[i-1]:
                return False
        
        return True

'''
Another method:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def Valid(self,root,min,max):
        if root is None:
            return True
        if root.val<=min or root.val>=max:
            return False
        return self.Valid(root.left,min,root.val) and self.Valid(root.right,root.val,max)
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        Min = -10**10
        Max = 10**10
        return self.Valid(root, Min, Max)
'''


'''
Test Case:
'''
if __name__ == '__main__':
    