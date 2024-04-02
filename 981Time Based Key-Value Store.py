class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = [(value, timestamp)]
        else:
            self.dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        else:
            cur_value_times = self.dict[key]
        def search(value_times, target: int) -> int:
            left = 0
            right = len(value_times) - 1
            if value_times[left][1] > target:
                return ""
            while left <= right:
                half = (left + right) // 2
                if(target == value_times[half][1]):
                    return value_times[half][0]
                elif target < value_times[half][1]:
                    right = half - 1
                elif target > value_times[half][1]:
                    left = half - 1
            return value_times[right][0]
        return search(cur_value_times, timestamp)



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
    
# buildin funciton
class TimeMap:

    def __init__(self):
        self.meta = collections.defaultdict(list)
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.meta[key].append(timestamp)
        self.data[key].append(value)


    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect(self.meta[key], timestamp)
        if idx == 0:
            return ''
        return self.data[key][idx - 1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)