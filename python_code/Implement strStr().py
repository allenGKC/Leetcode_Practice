'''
Problem:Implement strStr()
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1 = len(haystack)
        l2 = len(needle)
        if l1<l2:
            return -1
        for i in range(l1-l2+1):
            if haystack[i:i+l2]==needle:
                return i
        return -1
'''
Test Case:
'''
if __name__ == '__main__':
    