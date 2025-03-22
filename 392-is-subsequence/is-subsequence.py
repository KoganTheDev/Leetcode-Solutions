class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:  # if s is empty, return True
            return True
        
        s_index = 0
        
        for i in range(len(t)):
            if s[s_index] == t[i]:
                s_index += 1
                if s_index == len(s):  # Check if all characters in s have been matched
                    return True

        return False