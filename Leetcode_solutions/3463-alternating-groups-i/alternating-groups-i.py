class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        alternating_groups_counter = 0
        
        for i in range(len(colors)):
            #Edge case 1:
            if i == 0:
                if colors[i] != colors[len(colors) - 1] and colors[i] != colors[i + 1]:
                    alternating_groups_counter += 1
            elif i == len(colors) - 1:
                last_index = len(colors) - 1
                if colors[last_index] != colors[last_index - 1] and colors[last_index] != colors[0]:
                    alternating_groups_counter += 1
            else:
                if colors[i] != colors[i -1] and colors[i] != colors[i +1]:
                    alternating_groups_counter += 1
        
        return alternating_groups_counter