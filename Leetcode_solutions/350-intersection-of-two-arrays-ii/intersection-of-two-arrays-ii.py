class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        number_dict = dict()
        result_list = list()
        
        
        # Add elements from nums 1 to a dictionary
        for number in nums1:
            if number not in number_dict:
                number_dict[number] = 1
            elif number in number_dict:
                number_dict[number] += 1
        
        # Grab the numbers that are also in nums 2 by the amount there are in the intersection.
        for number in nums2:
            if (number in number_dict) and (number_dict[number] > 0):
                result_list.append(number)
                number_dict[number] -= 1 # Decrease the possible amount of numbers of that type in the intersection.
        
        return result_list