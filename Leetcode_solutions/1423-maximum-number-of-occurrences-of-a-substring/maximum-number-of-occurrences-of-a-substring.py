class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        substrings_dictionary = dict()
        for window_size in range(minSize, maxSize + 1): # Iterate through each possible window size
            i = 0
            while (i <= len(s) - window_size):
                window = s[i:i+window_size]
                
                if window in substrings_dictionary:
                    substrings_dictionary[window] += 1
                # The window is not in the dictionary therefore we need to check if it`s a valid option`    
                else:
                    letters_set = set()
                    letters_in_window_count = 0
                    for letter in window:
                        if letter not in letters_set:
                            letters_in_window_count += 1
                            letters_set.add(letter)
                    
                    # Check if string is valid meaning the amount of unique characters is less or equal to maxLetters
                    if letters_in_window_count <= maxLetters:
                        substrings_dictionary[window] = 1
                        
                i += 1
        return max(substrings_dictionary.values()) if substrings_dictionary else 0

                