class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        integer_as_string = str(x)
        return integer_as_string == integer_as_string[::-1]