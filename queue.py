class Queue():
    def __init__(self):
        self.queue =[]

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) > 0:
            self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def __str__(self):
        values = [str(x) for x in self.queue]
        return ' '.join(values)

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q)