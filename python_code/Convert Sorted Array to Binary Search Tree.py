'''
Problem:Convert Sorted Array to Binary Search Tree
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        mid=len(nums)//2
        node=TreeNode(nums[mid])
        node.left=self.sortedArrayToBST(nums[:mid])
        node.right=self.sortedArrayToBST(nums[mid+1:])
        return node
        
'''
Test Case:
'''
if __name__ == '__main__':
    