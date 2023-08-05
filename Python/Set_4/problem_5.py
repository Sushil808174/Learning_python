class QueueUsingStack:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, item):
        self.stack_enqueue.append(item)

    def dequeue(self):
        if not self.stack_dequeue:
            # Move elements from stack_enqueue to stack_dequeue
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())

        if self.stack_dequeue:
            return self.stack_dequeue.pop()

        return None

# Test the implementation
queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1
queue.dequeue()
print(queue.dequeue())
queue.enqueue(3)
print(queue.dequeue()) 
print(queue.dequeue()) 
print(queue.dequeue()) 
