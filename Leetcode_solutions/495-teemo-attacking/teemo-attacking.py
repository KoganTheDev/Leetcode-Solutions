class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        number_seconds = 0
        
        for attack in range(len(timeSeries) - 1):
            attacked_at = timeSeries[attack]
            next_attack = timeSeries[attack + 1]
            
            if next_attack < (attacked_at + duration): # Teemo attacked before the duration's timeout
                number_seconds += next_attack - attacked_at # Time diff until the poison's effect reset.
            else:
                number_seconds += duration
                
        number_seconds += duration # Last attack's duration
        return number_seconds