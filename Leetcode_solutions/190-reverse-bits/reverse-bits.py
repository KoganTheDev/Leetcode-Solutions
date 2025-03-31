class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        
        for i in range(32):  # Iterate through all 32 bits
            result = (result << 1) | (n & 1)  # Shift result left and add the least significant bit of n
            n >>= 1  # Shift n right to process the next bit
        
        return result