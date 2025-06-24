# 853. Car Fleet (Medium)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # No hints
        # No compile
        
        num_cars = len(position)

        stack = []
        eta = [(target-position[i])/speed[i] for i in range(num_cars)]
        stack = zip(position, eta)
        stack = sorted(stack, key=lambda car: car[0])

        cur_eta = 0
        num_fleets = 0
        while stack:
            pos, eta = stack.pop()
            if cur_eta < eta:
                cur_eta = eta
                num_fleets += 1 
        
        return num_fleets
