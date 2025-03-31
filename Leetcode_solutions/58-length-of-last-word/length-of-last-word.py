class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_word_length = 0
        
        if not s:
            return 0
        
        for char in s[::-1]:
            if char == ' ' and last_word_length > 0: # Currently on the last word.add()
                break
            elif char != ' ':
                last_word_length += 1
                
        return last_word_length