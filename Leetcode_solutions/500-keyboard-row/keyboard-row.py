class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm"
        ]
        
        for word in words:
            for row in rows:
                if all([x in row for x in word.lower()]):
                    ans.append(word)
        return ans