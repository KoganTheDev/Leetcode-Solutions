class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        maxPrefix = ""
        if not strs:
            return maxPrefix
        minLen = min([len(s) for s in strs])
        for i in range(minLen):
            if len(set([s[i] for s in strs])) == 1:
                maxPrefix += strs[0][i]
            else:
                break
        return maxPrefix
    