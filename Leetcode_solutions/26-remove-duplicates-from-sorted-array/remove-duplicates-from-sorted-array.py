class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        index_to_replace = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index_to_replace] = nums[i]
                index_to_replace += 1
                
        return index_to_replace