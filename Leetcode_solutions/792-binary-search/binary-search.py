class Solution:
    def search(self, nums: List[int], target: int) -> int:
        array_length = len(nums)
        left_ptr = 0
        right_ptr = array_length - 1
        
        # Start the algorithm
        while (left_ptr <= right_ptr):
            # Calculate middle index
            mid = (left_ptr + right_ptr) // 2
            
            # Found in the middle
            if (nums[mid] == target):
                return mid
            # Drop left section
            elif (nums[mid] < target):
                left_ptr = mid + 1
            # Drop right section
            elif (nums[mid] > target):
                right_ptr = mid - 1
                
        # Not found - return -1
        return -1