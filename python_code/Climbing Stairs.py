'''
Problem:Climbing Stairs 
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        pre,next,cur = 1,2,0
        
        for i in range(2,n):
            cur = pre+next
            pre,next =next,cur
        
        return cur
'''
Test Case:
'''
if __name__ == '__main__':
    