class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        current_product = 1
        left_ptr = 0
        result = 0
        
        for right_ptr in range(len(nums)):
            current_product *= nums[right_ptr]
            
            # Shrink the window while product is too large
            while current_product >= k:
                current_product //= nums[left_ptr]
                left_ptr += 1
            
            # Every subarray ending at right_ptr and starting from left_ptr...right_ptr is valid
            result += (right_ptr - left_ptr + 1)
        
        return result
