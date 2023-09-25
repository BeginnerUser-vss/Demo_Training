class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Cannot dequeue from an empty queue.")
    def is_empty(self):
        return len(self.items) == 0
    def queue_front(self):
        return self.items[0]
    def queue_last(self):
        return self.items[-1]

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

print("Current Queue:", queue.items)
dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)
dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)
print("Updated Queue:", queue.items)
print("Front of the Queue is ", queue.queue_front())