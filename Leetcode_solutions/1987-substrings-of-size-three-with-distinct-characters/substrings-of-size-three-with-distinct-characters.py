class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        good_substrings_counter = 0

        for i in range(len(s) - 2):  # Run in windows of 3 characters
            substring = s[i:i + 3]
            if len(set(substring)) == 3:
                good_substrings_counter += 1  # found a good substring

        return good_substrings_counter
