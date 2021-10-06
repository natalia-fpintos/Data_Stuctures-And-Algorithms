class GameObject:
    def __init__(self, key, name):
        self.key = key
        self.name = name


class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None for _ in range(size)]

    def display(self):
        for k, v in enumerate(self.data):
            if v is not None:
                print(f"Index: {k}. Key: {v.key}. Name: {v.name}.")

    def hash_function(self, key):
        pass

    def insert(self, item):
        pass


if __name__ == "__main__":
    pass