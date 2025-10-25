class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        if not s:
            return 0
        
        char_map = {}
        idx_left = 0

        for idx_right in range(len(s)):
            if s[idx_right] in char_map and char_map[s[idx_right]] >= idx_left:
                idx_left = char_map[s[idx_right]] + 1

            char_map[s[idx_right]] = idx_right
            max_length = max(max_length, idx_right - idx_left + 1)

        return max_length
