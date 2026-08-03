class MinStack:

    def __init__(self):
        self.stack = []
        self.minStk = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStk[-1] if self.minStk else val)
        self.minStk.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStk.pop()

    def top(self) -> int:
        return self.stack[-1]
            

    def getMin(self) -> int:
        return self.minStk[-1]
        
