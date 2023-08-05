from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        self.queue2.put(item)
        while not self.queue1.empty():
            self.queue2.put(self.queue1.get())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if self.queue1.empty():
            return None
        return self.queue1.get()

# Test the StackUsingQueue class
stack = StackUsingQueue()
output = []

stack.push(1)
output.append(stack.pop())
output.append(stack.pop())

stack.push(3)
output.append(stack.pop())

output.append(stack.pop())
output.append(stack.pop())
output.append(stack.pop())

print(", ".join(map(str,output)))