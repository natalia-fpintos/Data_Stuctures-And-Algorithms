class PriorityQueue:
    # Sorted in descending order
    def __init__(self, size):
        self.count = 0
        self.data = [None for _ in range(size)]
        self.size = size
        self.front = 0
        self.rear = -1

    def insert(self, item):
        if self.is_empty():
            self.data[0] = item
        else:
            insert_at = self.front
            for i in range(self.last_index(), self.front - 1, -1):
                # Move smaller items to the end of the list
                if item > self.data[i]:
                    self.data[i+1] = self.data[i]
                    continue
                # If inserted item is equal or smaller, insert to the right
                else:
                    insert_at = i + 1
                    break

            self.data[insert_at] = item

        self.count += 1
        self.rear = self.rear + 1 if self.rear < self.size - 1 else 0
        print('current priority queue: {}'.format(self.data))

    def remove(self):
        self.count -= 1
        item = self.data[self.front]
        self.data[self.front] = None
        self.front = self.front + 1 if self.front < self.size - 1 else 0
        print('current priority queue: {}'.format(self.data))
        return item

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def last_index(self):
        return self.rear


if __name__ == "__main__":
    p_queue = PriorityQueue(10)
    p_queue.insert(3)
    p_queue.insert(5)
    p_queue.insert(2)
    p_queue.insert(1)
    p_queue.insert(5)
    p_queue.insert(4)
    p_queue.remove()
    p_queue.insert(10)
    p_queue.remove()
    p_queue.remove()
    p_queue.insert(2)
    p_queue.insert(7)
    p_queue.insert(6)
    p_queue.insert(8)
