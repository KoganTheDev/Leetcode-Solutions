class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_sorted = sorted(nums)  # Sort the list
        relevant_indexes = []
        
        # Use binary search to find the first target
        first_index = self.binarySearch(nums_sorted, 0, len(nums_sorted) - 1, target)
        
        # Target not found
        if first_index == -1:
            return []
        
        # Find all relevant indices for the target in the sorted array
        # Now, find the range of occurrences of the target
        for i in range(first_index, len(nums_sorted)):
            if nums_sorted[i] == target:
                relevant_indexes.append(i)
            else:
                break
        
        # Collect all left occurrences as well (we have to handle left-side expansion separately)
        for i in range(first_index - 1, -1, -1):
            if nums_sorted[i] == target:
                relevant_indexes.insert(0, i)  # Insert at the beginning to maintain sorted order
            else:
                break
        
        return relevant_indexes
        
    def binarySearch(self, arr, low, high, target):
        while low <= high:
            mid = low + (high - low) // 2
            
            # Check if the target is in the middle
            if arr[mid] == target:
                # Look for the first occurrence of target
                if mid == low or arr[mid - 1] != target:
                    return mid  # Return the index of the first occurrence
                else:
                    high = mid - 1  # Continue to search to the left
                
            # If the target is greater, ignore the left half
            elif arr[mid] < target:
                low = mid + 1
                
            # If the target is smaller, ignore the right half 
            else:
                high = mid - 1
        
        return -1  # Target not found
