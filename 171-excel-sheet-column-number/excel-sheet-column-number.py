class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        column_number = 0
        offset = ord('A') - 1
        base26 = 26
        exponent = 0
        
        if not columnTitle:
            return column_number
        
        # Calculate the result integer using a base algorithm e.g binary, decimal, hexadecimal
        for character in columnTitle[::-1]: # Read from right to left. in binary from LSB to MSB
            column_number += (ord(character) - offset) * base26 ** exponent
            exponent += 1
        
        return column_number