class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1:
            return 1
        
        trust_counts = {i: 0 for i in range(1, n + 1)}
        
        for a, b in trust:
            trust_counts[a] -= 1
            trust_counts[b] += 1
        
        for person in range(1, n + 1):
            if trust_counts[person] == n - 1:
                return person
        
        return -1
        