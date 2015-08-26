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

if __name__ == '__main__':
    s = Solution()
    array = [3,4,1]
    r = s.twoSum(array,7)
    print r