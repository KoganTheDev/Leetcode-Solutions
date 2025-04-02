# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first, last = 1, n

        while first < last:
            mid = first + (last - first) // 2

            if isBadVersion(mid):
                last = mid  # The first bad version could be mid or before.
            else:
                first = mid + 1  # The first bad version must be after mid.

        return first  # At the end, first will be the first bad version.