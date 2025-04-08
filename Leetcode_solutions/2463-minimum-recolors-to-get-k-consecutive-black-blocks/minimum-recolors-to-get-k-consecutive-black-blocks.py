class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        current_recolor = blocks[:k].count('W')
        minimum_recolor = current_recolor

        for i in range(1, len(blocks) - k + 1):
            if blocks[i - 1] == 'W':
                current_recolor -= 1
            if blocks[i + k - 1] == 'W':
                current_recolor += 1

            minimum_recolor = min(minimum_recolor, current_recolor)

        return minimum_recolor
