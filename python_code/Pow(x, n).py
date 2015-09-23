'''
Problem:Pow(x, n)
Implement pow(x, n).
'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n<0:
            return 1/self.myPow(x, -n)
        if n == 1:
            return x
        if not n%2:
            return self.myPow(x*x, n/2) 
        
        return x*self.myPow(x*x, n/2)
        '''
        short method:
        return x ** n
        '''
'''
Test Case:
'''
if __name__ == '__main__':
    