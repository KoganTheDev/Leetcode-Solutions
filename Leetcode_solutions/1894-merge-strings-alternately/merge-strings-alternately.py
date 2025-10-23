class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1_length = len(word1)
        word2_length = len(word2)
        result = []
        
        # Empty first word
        if (word1_length == 0):
            return word2
        # Empty second word
        if (word2_length == 0):
            return word1
        
        min_length = min(word1_length, word2_length)
        
        for i in range(min_length):
            # Alternate
            result.append(word1[i]) 
            result.append(word2[i]) 
            
        # Append the remainder
        if word1_length > min_length:
            result.append(word1[min_length:])
        elif word2_length > min_length:
            result.append(word2[min_length:])
        
        # Stringify 
        return "".join(result)
            
            
        
            
        
        