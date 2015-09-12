'''
Problem:Two Sum
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        number = sorted(nums)
        length = len(nums)
        left = 0
        right = length-1
        index = []
        while left < right:
            sum = number[left]+number[right]
            if sum==target:
                for i in range(length):
                    if nums[i]==number[left]:
                        index.append(i+1)
                    elif nums[i]==number[right]:
                        index.append(i+1)
                    if len(index)==2:
                        break
                break
            elif sum>target:
                right-=1
            else:
                left+=1
        result = tuple(index)
        return result
'''
Test Case:
'''
if __name__ == '__main__':
    s = Solution()
    array = [3,4,1]
    r = s.twoSum(array,7)
    print r
