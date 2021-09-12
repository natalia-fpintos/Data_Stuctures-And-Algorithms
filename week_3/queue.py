class queue:
    def __init__(self, size):
        self.queue = [None for _ in range(size)]
        self.front = 0
        self.rear = -1
        self.count = 0
        self.size = size

    def insert(self, item):
        # Go back to the front if we are at the end of the queue
        if self.rear == self.size - 1:
            self.rear = -1
        self.rear += 1
        self.queue[self.rear] = item
        self.count += 1

        print('current queue: {}'.format(self.queue))

    def remove(self):
        item = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.size - 1:
            self.front = -1
        self.front += 1
        self.count -= 1
        return item

        print('current queue: {}'.format(self.queue))

    def peek_front(self):
        return self.queue[self.front]

    def is_empty(self):
        return self.count == 0



if __name__ == '__main__':
    my_queue = queue(4)
    my_queue.insert(1)
    my_queue.insert(2)
    my_queue.insert(3)
    my_queue.insert(4)
    print(my_queue.remove())
    print(my_queue.remove())
    my_queue.insert(5)
    my_queue.insert(6)
    print(my_queue.remove())

