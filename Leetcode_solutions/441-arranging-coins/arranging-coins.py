class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        rows_filled = 0
        current_row = 1
        
        while n >= current_row:
            n -= current_row
            rows_filled += 1
            current_row += 1
            
        return rows_filled
