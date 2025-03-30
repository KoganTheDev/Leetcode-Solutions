class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letters_in_s = dict()  # Corrected the dictionary initialization
        
        for char in s:
            if char not in letters_in_s:
                letters_in_s[char] = 1  # Initialize the count
            else:
                letters_in_s[char] += 1
        
        for char in t:
            if char not in letters_in_s:
                return False
            elif letters_in_s[char] > 0:
                letters_in_s[char] -= 1
            else:
                return False
        
        # Ensure all counts in the dictionary are zero for the strings to be anagrams
        return all(value == 0 for value in letters_in_s.values())