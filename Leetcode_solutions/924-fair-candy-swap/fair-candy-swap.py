class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)
        diff = (alice_sum - bob_sum) // 2

        # Sort Bob's candies for binary search
        bob_sorted = sorted(bobSizes)

        for a in aliceSizes:
            b = a - diff
            if self.binarySearch(bob_sorted, 0, len(bob_sorted) - 1, b) != -1:
                return [a, b]
        
        return []

    def binarySearch(self, arr, low, high, target):
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
