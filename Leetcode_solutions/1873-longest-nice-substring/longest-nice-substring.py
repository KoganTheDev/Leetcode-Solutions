class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 1:
            return ""

        dictionary = dict()
        # Gather all the letters and put them in a dictionary
        for c in s:
            if c not in dictionary:
                dictionary[c] = 0
            else:
                dictionary[c] += 1
        
        is_broken = False
        i = 0
        while (i < len(s)):
            if s[i].islower() and s[i].upper() in dictionary.keys(): 
                pass
            elif s[i].isupper() and s[i].lower() in dictionary.keys(): 
                pass
            else:
                is_broken = True
                break
            i += 1

        if not is_broken: 
            return s
        
        # Divide and conquer using recursion.
        longest_nice_substr_1 = self.longestNiceSubstring(s[:i])
        longest_nice_substr_2 = self.longestNiceSubstring(s[i+1:])
        
        if len(longest_nice_substr_1)>=len(longest_nice_substr_2): 
            return longest_nice_substr_1
        else: 
            return longest_nice_substr_2