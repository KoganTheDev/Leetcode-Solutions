class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        number_dictionary = dict()
        
        for number in nums:
            if number not in number_dictionary:
                number_dictionary[number] = 1
            else: # Number is in the dictionary therefore we encountered another occurrence.
                return True
        return False # No duplicates found.