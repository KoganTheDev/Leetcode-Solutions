class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """

        min_value = float('inf') # Initial value set to infinity
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                sub_array = nums[i:j]
                sub_array_sum = sum(sub_array)
                
                # Check if the subarray size is between l and r (inclusive) and sum is greater than 0
                if l <= len(sub_array) <= r and sub_array_sum > 0 and sub_array_sum < min_value:
                    min_value = sub_array_sum
        
        if min_value == float('inf'): # No relevant value was assigned.
            return -1
        
        return min_value