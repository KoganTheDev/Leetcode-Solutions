class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        min_length = float('inf')

        for l in range(n):
            current_or = 0
            for r in range(l, n):
                current_or |= nums[r]
                if current_or >= k:
                    min_length = min(min_length, r - l + 1)
                    break  # Found a valid subarray starting at `l`, no need to check longer ones

        return min_length if min_length != float('inf') else -1
