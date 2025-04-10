class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        max_score = 0

        # Initial window: take the first k cards
        current_sum = sum(cardPoints[:k])
        max_score = current_sum

        # Now slide the window: remove cards from the front, add from the back
        for i in range(1, k + 1):
            current_sum = current_sum - cardPoints[k - i] + cardPoints[-i]
            max_score = max(max_score, current_sum)

        return max_score
