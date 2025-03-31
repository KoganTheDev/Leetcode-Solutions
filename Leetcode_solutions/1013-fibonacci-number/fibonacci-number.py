class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        opt = [0, 1]
        
        for i in range(2, n + 1):
            opt.append(opt[i - 1] + opt[i - 2])    
        
        return opt[n]