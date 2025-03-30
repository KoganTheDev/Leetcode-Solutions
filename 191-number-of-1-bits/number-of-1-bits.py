class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        Intuition:
        create a counter
        check if odd by using modulo
        if odd, counter++
        
        move bits to the right -> therefore absorb the lsb
        do so until n is equal to 0.
        '''
        counter = 0
        
        while n > 0:
            if n % 2 == 1: # Odd number
                counter += 1
            #absorb lsb
            n >>= 1
            
        return counter