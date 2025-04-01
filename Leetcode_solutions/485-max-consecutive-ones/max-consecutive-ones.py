class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        count = 0
        
        for number in nums:
            if number == 1:
                count += 1
            if number == 0: # Reset count
                count = 0
            
            max_count = max(max_count, count)
            
        return max_count