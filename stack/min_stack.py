# 155. Min Stack (Medium)

class MinStack:

    # Hint 1
    # Compiled to Debug

    def __init__(self):
        self.nums = collections.deque()
        self.minNums = collections.deque()

    def push(self, val: int) -> None:
        self.nums.appendleft(val)
        if not self.minNums or val <= self.minNums[0]:
            self.minNums.appendleft(val)

    def pop(self) -> None:
        num = self.nums.popleft()
        if num == self.minNums[0]:
            self.minNums.popleft()
        
    def top(self) -> int:
        return self.nums[0]

    def getMin(self) -> int:
        return self.minNums[0]