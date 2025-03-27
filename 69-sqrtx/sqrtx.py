class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x  # The square root of 0 is 0, and the square root of 1 is 1.

        left, right = 0, x // 2  # The square root of x is at most x // 2 for x >= 2.
        result = 0

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid  # Exact square root found.
            elif square < x:
                result = mid  # Store the current mid as a potential result.
                left = mid + 1  # Narrow the search to the right half.
            else:
                right = mid - 1  # Narrow the search to the left half.

        return result  # Return the integer part of the square root.