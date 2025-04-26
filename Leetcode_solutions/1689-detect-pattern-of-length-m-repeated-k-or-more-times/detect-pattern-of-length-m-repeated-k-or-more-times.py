class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        arr_length = len(arr)
        
        if m > arr_length:
            return False
        
        # Go through every starting point
        for i in range(arr_length - m * k + 1):  # Important: Stop early enough
            pattern = arr[i:i+m]
            count = 1  # We saw the first pattern at position i
            
            # Check following patterns
            for j in range(1, k):
                next_pattern = arr[i + j*m : i + (j+1)*m]
                
                if next_pattern == pattern:
                    count += 1
                else:
                    break  # No point in continuing
            
            if count == k:
                return True
        
        return False
