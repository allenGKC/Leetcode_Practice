'''
Problem:3Sum
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        length = len(nums)
        if length<3:
            return result
        elif length == 3:
            if sum(nums)==0:
                return [nums]
            else:
                return result

        
        for i in xrange(length-2):
            j = i+1
            k = length-1
            while j<k:
                t = nums[i]+nums[j]+nums[k]
                if t == 0:
                    result.append((nums[i],nums[j],nums[k]))
                if t > 0:
                    k-= 1
                else:
                    j += 1
        return list(set(result))

'''
Test Case:
'''
if __name__ == '__main__':
    