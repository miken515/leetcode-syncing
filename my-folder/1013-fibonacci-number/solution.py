class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
        # else:
        #     return self.fib(n-1) + self.fib(n-2)

        if n == 0:
            return 0
        if n == 1:
            return 1

        prev = 0
        cur = 1

        for i in range(2, n+1):
            prev, cur = cur, prev+cur
        
        return cur
