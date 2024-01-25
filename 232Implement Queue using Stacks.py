'''
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)


    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        temp = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return temp

    def peek(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        temp = self.stack2.pop()
        self.stack2.append(temp)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return temp

    def empty(self) -> bool:
        return not self.stack1
'''
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out