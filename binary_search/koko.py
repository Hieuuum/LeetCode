# 875. Koko Eating Bananas (Medium)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Hints
        # Compile to Debug
        
        min_speed = 1
        max_speed = max(piles)
        speed_candidate = 0
        
        while min_speed <= max_speed:
            time = 0
            speed = (min_speed + max_speed) // 2
            for pile in piles:
                time += math.ceil(pile / speed)
            
            if time <= h:
                speed_candidate = speed
                max_speed = speed - 1
            else:
                min_speed = speed + 1

        return speed_candidate