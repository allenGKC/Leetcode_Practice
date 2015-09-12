'''
Problem:String to Integer (atoi)
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
'''
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        length = len(str)
        if length == 0:
            return 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        tmp = '0'
        i = 0
        if str[0] in '+-':
            tmp = str[0]
            i = 1
        for i in xrange(i,length):
            if str[i].isdigit():
                tmp+=str[i]
            else:
                break
        if len(tmp) > 1:
            tmp = (int)(tmp)
        else:
            return 0
        if tmp > INT_MAX > 0:
            return INT_MAX
        elif tmp < INT_MIN < 0 :
            return INT_MIN
        else:
            return tmp
'''
Test Case:
'''
if __name__ == '__main__':
    