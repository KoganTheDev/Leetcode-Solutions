class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        minimum_cost = 0
        sorted_cost = sorted(cost, reverse= True)
        
        for i in range(len(sorted_cost)):
            # Skip on each third candy
            if (i + 1) % 3 == 0:
                continue
            
            minimum_cost += sorted_cost[i]
            
        return minimum_cost