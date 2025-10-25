class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first_index = {}
        last_index = {}
        count = {}

        for i, num in enumerate(nums):
            if num not in first_index:
                first_index[num] = i
            # Update last index seen
            last_index[num] = i
            count[num] = count.get(num, 0) + 1

        # Find the maximum degree
        degree = max(count.values())
        min_length = len(nums)

        # Find the numbers that have the same degree as the array and find the smallest subarray
        for num in count:
            if count[num] == degree:
                min_length = min(min_length, last_index[num] - first_index[num] + 1)

        return min_length