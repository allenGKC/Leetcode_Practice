'''
Problem:Single Number
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if None==nums:
            return "false"
            
        arr = sorted(nums)
        i = 0
        length = len(nums)
        while(i<length-2):
            if arr[i]==arr[i+1]:
                i+=2
            else:
                return arr[i]
        return arr[i]
        '''
        Another Solution:
        
        length = len(nums)
        result = 0
        for i in range(0,length):
            result = result^nums[i]
        return result 
        '''
'''
Test Case:
'''
if __name__ == '__main__':
    s = Solution()
    array = [1,1,2,4,4]
    r = s.singleNumber(array)
    print r