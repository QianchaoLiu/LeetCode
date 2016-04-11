class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return True if (n>0) and (not(n&(n-1))) else False
        # using bit manipulation to check wheter power(x,2)==n or not
        
