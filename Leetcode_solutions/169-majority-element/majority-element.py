class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers_and_their_appearances = dict()
        majority_element_lower_bound = len(nums) // 2 # By the definition of the majority element.
        
        for number in nums:
            if number in numbers_and_their_appearances: # The number is in the dictionary
                numbers_and_their_appearances[number] += 1
            else: # The number is not in the dictionary therefore we need to initialize it.
                numbers_and_their_appearances[number] = 1
        
        for key in numbers_and_their_appearances:
            if (numbers_and_their_appearances.get(key) >= majority_element_lower_bound):
                majority_element = key
                majority_element_lower_bound = numbers_and_their_appearances.get(key) # Update lower bound for the current possible candidate.

        return majority_element