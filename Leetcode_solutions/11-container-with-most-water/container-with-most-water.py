class Solution:
    def maxArea(self, height: List[int]) -> int:
        curr_max = 0
        
        # Initialize pointers
        left_ptr = 0
        right_ptr = len(height) - 1
        
        while(left_ptr != right_ptr):
            # Calculate current max
            # Find the minimum bar
            min_bar = min(height[left_ptr], height[right_ptr])
            curr_max = max(curr_max, min_bar * (right_ptr - left_ptr))
            
            # Shift pointers - try finding a higher value for a bar
            left_bar = height[left_ptr]
            right_bar = height[right_ptr]
            
            if (left_bar < right_bar): # Move left ptr
                left_ptr += 1
            elif (left_bar > right_bar): # Move right ptr
                right_ptr -= 1
            else: # Move a pointer arbitrarily
                left_ptr += 1
        
        return curr_max
                