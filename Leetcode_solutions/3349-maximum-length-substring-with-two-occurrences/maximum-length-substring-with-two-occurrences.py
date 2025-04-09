class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maximum_length = 0

        for l in range(len(s)):
            letter_counter_dictionary = dict()
            current_length = 0
            for r in range(l, len(s)):
                if s[r] not in letter_counter_dictionary:
                    letter_counter_dictionary[s[r]] = 1
                else:
                    if letter_counter_dictionary[s[r]] == 2:
                        break
                    letter_counter_dictionary[s[r]] += 1
                current_length += 1
            maximum_length = max(maximum_length, current_length)

        return maximum_length
