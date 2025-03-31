class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        letter_array = []
        
        while columnNumber > 0:
            columnNumber -= 1  # Adjust for 1-based indexing
            letter_array.append(chr(65 + (columnNumber % 26)))  # Convert to letter
            columnNumber //= 26  # Move to the next "digit"
        
        return ''.join(letter_array[::-1])  # Reverse and join the letters