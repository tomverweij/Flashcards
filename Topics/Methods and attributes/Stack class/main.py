class Stack:
    els = []
    
    def __init__(self):
        pass

    def push(self, el):
        self.els.append(el)

    def pop(self):
        return self.els.pop()

    def peek(self):
        return len(self.els)-1

    def is_empty(self):
        return True if len(self.els) == 0 else False


# stack = Stack()
# print(stack.is_empty())
# stack.push(0)
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# print(stack.pop())
# print(stack.pop())
# print(stack.peek())
# print(stack.pop())
# print(stack.is_empty())