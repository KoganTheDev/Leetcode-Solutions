class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        remainder = 1
        numbers_after_plus_one = {
            0: 1,
            1: 2,
            2: 3,
            3: 4,
            4: 5,
            5: 6,
            6: 7,
            7: 8,
            8: 9,
            9: 0  # 9 becomes 0 and we need to handle the carry
        }
        
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = numbers_after_plus_one[digits[i]]
            if digits[i] != 0:
                remainder = 0
                break
        
        if remainder == 1:  # Special case: remainder on the last digit
            digits = [1] + digits
            
        return digits