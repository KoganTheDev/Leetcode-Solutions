class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ord_sum = 0
        for ch in t:
            ord_sum += ord(ch)
        for ch in s:
            ord_sum -= ord(ch)
        return (chr(ord_sum))