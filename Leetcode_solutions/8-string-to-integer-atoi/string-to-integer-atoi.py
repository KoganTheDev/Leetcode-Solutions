class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        result_as_integer = 0
        sign_flag = 1
        numbers = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }
        
        s = s.strip()  # Delete leading and trailing whitespaces.
        
        if not s:
            return 0
        
        if s[0] == '-':  # Fetch the sign of the number
            sign_flag = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        for char in s:
            if char.isdigit():
                result_as_integer = result_as_integer * 10 + numbers[char]
            else:
                break
        
        result_as_integer *= sign_flag
        
        # Clamp the result to the 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result_as_integer > INT_MAX:
            return INT_MAX
        if result_as_integer < INT_MIN:
            return INT_MIN
        
        return result_as_integer