'''
Problem:Number of 1 Bits
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0 
        binary_num = bin(n)
        binary_str = binary_num.split('b')[1]
        for i in range(len(binary_str)):
            if binary_str[i] == "1":
                count +=1
        return count
		'''
		other methods
		return str(bin(n)).count('1')
		'''       
'''
Test Case:
'''
if __name__ == '__main__':
    