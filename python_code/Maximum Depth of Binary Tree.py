'''
Problem:Maximum Depth of Binary Tree  
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
'''
Test Case:
'''
if __name__ == '__main__':
    