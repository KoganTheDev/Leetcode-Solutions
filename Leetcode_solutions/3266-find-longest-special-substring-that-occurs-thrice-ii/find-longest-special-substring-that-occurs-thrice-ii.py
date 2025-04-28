class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        special_substrings = defaultdict(int)
        
        start = 0
        while start < len(s):
            curr = start
            while curr < len(s) - 1 and s[curr] == s[curr + 1]:
                curr += 1
            
            window_size = curr + 1 - start
            for length in range(1, window_size + 1):
                special_substrings[(s[start], length)] += window_size + 1 - length
                
            start = curr + 1

        res = -1
        for k in special_substrings:
            if special_substrings[k] >= 3:
                res = max(res, k[1])
                
        return res
