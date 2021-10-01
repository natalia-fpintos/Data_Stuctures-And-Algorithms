class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack_data = [None for _ in range(max_size)]
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def peek(self):
        return self.stack_data[self.top]

    def pop(self):
        if not self.is_empty():
            item = self.peek()
            self.top -= 1
            return item
        print("The stack is empty: cannot pop item")

    def push(self, value):
        if not self.is_full():
            self.top += 1
            self.stack_data[self.top] = value
        else:
            print("The stack is full: cannot push item")


class Link:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.first = None

    def insert(self, new_link):
        new_link.next = self.first
        self.first = new_link

    def remove(self):
        item = self.first
        self.first = self.first.next
        return item

    def display(self):
        current = self.first
        while current is not None:
            print(current.data)
            current = current.next


if __name__ == "__main__":
    print("Stack exercises:")

    a_stack = Stack(5)

    for i in range(6):
        a_stack.push(i)
    
    print(a_stack.stack_data)

    for _ in range(6):
        print(f"Stack item popped: {a_stack.pop()}")

    print("Linked list stack exercises:")

    a_linked_stack = LinkedStack()

    for i in range(10):
        a_linked_stack.insert(Link(i))

    a_linked_stack.display()

    while a_linked_stack.first is not None:
        print(f"Stack link popped: {a_linked_stack.remove().data}")
