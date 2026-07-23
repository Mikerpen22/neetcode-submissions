from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp: 
            return ""
        
        stored = self.mp[key]   # [('happy', 1), ('sad', 2)....]
        l, r = 0, len(stored)-1
        ans = ""
        while l <= r:
            mid = l + (r-l)//2
            if stored[mid][1] == timestamp:
                return stored[mid][0]
            elif stored[mid][1] < timestamp:
                ans = stored[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return ans