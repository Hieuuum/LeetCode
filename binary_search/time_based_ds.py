# 981. Time Based Key-Value Store (Medium)

class TimeMap:

    def __init__(self):
        self.time_dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_dict:
            self.time_dict[key] = []
        self.time_dict[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_dict:
            return ""

        val = self.time_dict[key]
        if val[0][0] > timestamp:
            return ""
        
        res = ""
        l, r = 0, len(val) - 1

        while l <= r:
            mid = (l + r) // 2
            if val[mid][0] <= timestamp:
                res = val[mid][1]
                l = mid + 1
            else:
                r = mid - 1
            
        return res

        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)