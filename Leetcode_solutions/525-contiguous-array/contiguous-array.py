class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeroes, ones = 0, 0
        result = 0
        
        diff_index = {} # count[1] - count[0] = index
        
        for i,n in enumerate(nums):
            if n == 0:
                zeroes += 1
            else:
                ones += 1
                
            if ones - zeroes not in diff_index:
                diff_index[ones - zeroes] = i
                
            if ones == zeroes:
                result = ones + zeroes
            else:
                index = diff_index[ones - zeroes]
                result = max(result, i - index)
        
        return result