class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        result = [0] * n
        
        for i in range(n):
            total = 0
            if k > 0:
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
            elif k < 0:
                for j in range(1, -k + 1):
                    total += code[(i - j) % n]
            # If k == 0, result[i] stays 0
            result[i] = total
        
        return result
