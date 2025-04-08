class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        longest_subarray_length = 0
        
        for l in range(len(nums)):
            if (nums[l] <= threshold) and (nums[l] % 2 == 0):
                current_longest = 1

                # Increase the size of the window
                for r in range(l, len(nums) - 1):
                    if (nums[r] <= threshold) and (nums[r + 1] <= threshold) and (nums[r] % 2 != nums[r + 1] % 2):
                        current_longest += 1
                    else:
                        break
            
                longest_subarray_length = max(longest_subarray_length, current_longest)
            
        return longest_subarray_length