class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        number_set = set()
        result_set = set()
        
        for number in nums1:
            number_set.add(number)
        
        for number in nums2:
            if number in number_set:
                result_set.add(number)
        
        res = list(result_set)
        
        return res