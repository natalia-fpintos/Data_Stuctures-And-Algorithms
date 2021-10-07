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
        return key % self.size

    def insert(self, item):
        key = item.key
        h = self.hash_function(key)

        while self.data[h] is not None:
            h += 1
            h %= self.size

        self.data[h] = item


if __name__ == "__main__":
    table = HashTable(17)
    table.insert(GameObject(10, "Bridge"))
    table.insert(GameObject(5, "Player"))
    table.insert(GameObject(30, "Tank"))
    table.insert(GameObject(16, "AI"))
    table.display()
