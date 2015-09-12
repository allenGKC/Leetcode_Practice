'''
Problem:Single Number II 
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = sorted(nums)
        length = len(nums)
        result = []
        i = 0
        if length==1:
        	return nums[0]
        while i<length-1:
			if arr[i]==arr[i+1]:
				i+=3
			else:
				result.append(arr[i])
				break
		
        if i==length-1:
            result.append(arr[i])
        
        return result

'''
Test Case:
'''
if __name__ == '__main__':
    s = Solution()
    array = [2,2,3,2]
    r = s.singleNumber(array)
    print r