class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:    
        left_ptr = 0
        max_length = 0
        zeros_in_window = 0

        for right_ptr in range(len(nums)):
            if nums[right_ptr] == 0:
                zeros_in_window += 1

            # If we have more than k zeros, shrink the window
            while zeros_in_window > k:
                if nums[left_ptr] == 0:
                    zeros_in_window -= 1
                left_ptr += 1

            # Update max length for every valid window
            max_length = max(max_length, right_ptr - left_ptr + 1)

        return max_length