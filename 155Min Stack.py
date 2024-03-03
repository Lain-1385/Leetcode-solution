class MinStack:

    def __init__(self):
        self.list = []
        self.min_val = []

    def push(self, val: int) -> None:
        self.list.append(val)
        if self.min_val == [] or self.min_val[-1] < val:
            self.min_val.append(val)
        else:
            self.min_val.append(self.min_val[-1])

    def pop(self) -> None:
        self.list.pop()
        self.min_val.pop()

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.min_val[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()