class FreqStack:

    def __init__(self):
        self.stack = []
        self.dict = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not val in dict:
            self.dict[val] = 1
        else:
            self.dict[val] += 1      

    def pop(self) -> int:
                


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()