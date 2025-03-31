class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number_dict = dict()
        
        for number in nums:
            number_dict[number] = 1

        #check all of the possible numbers
        for number in range(len(nums) + 1):
            if number not in number_dict:
                return number
            