class GameObject:
    def __init__(self, key, name):
        self.key = key
        self.name = name


class GameObjectStr:
    def __init__(self, key, name):
        self.key = str(key)
        self.name = name


class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None for _ in range(size)]

    def display(self):
        for k, v in enumerate(self.data):
            if v is not None:
                print(f"Index: {k}. Key: {v.key}. Name: {v.name}.")

    @staticmethod
    def display_item(item, index):
        print(f"Index: {index}. Key: {item.key}. Name: {item.name}.")

    def hash_function(self, key):
        # Simple hashing based on a number
        return key % self.size

    def insert(self, item):
        key = item.key
        h = self.hash_function(key)

        while self.data[h] is not None:
            h += 1
            print(f'Collision for item {item.name}')
            h %= self.size

        self.data[h] = item

    def find(self, key):
        hashed_key = self.hash_function(key)
        while self.data[hashed_key] is not None:
            if self.data[hashed_key].key == key:
                # Match found
                return self.data[hashed_key], hashed_key

            # Could not find a match, check the next item
            hashed_key += 1
            hashed_key %= self.size  # Don't go over the list bounds
        return None, None  # Could not find any matches

    def delete(self, key):
        found_item, index = self.find(key)
        if found_item is not None:
            print(f"Deleted item at index {index}")
            self.data[index] = None
        else:
            print("Cannot delete: item not found")
        return found_item


class HashTableStr(HashTable):
    def hash_function(self, key):
        # More complex hashing based on ascii values of a string
        str_key = str(key)
        result = 0
        for i, char in enumerate(reversed(str_key)):
            result += ord(char)  # Simpler option to cause collisions
            # result += ord(char) * (255 ** i)  # More complex, no collisions
        return result % self.size


if __name__ == "__main__":
    print("----- Exercise 1: Insert -----")
    table = HashTable(17)
    table.insert(GameObject(10, "Bridge"))
    table.insert(GameObject(5, "Player"))
    table.insert(GameObject(30, "Tank"))
    table.insert(GameObject(16, "AI"))
    table.insert(GameObject(16, "AI 2"))
    table.display()

    print("\n----- Exercise 2: Find -----")
    table.display_item(*table.find(30))

    print("\n----- Exercise 3: Delete -----")
    table.delete(8)
    table.delete(30)
    table.display()

    print("\n----- Exercise 4: Hashing -----")
    print("Create and display:")
    str_table = HashTableStr(14)
    str_table.insert(GameObjectStr('10', "Bridge"))
    str_table.insert(GameObjectStr('5', "Player"))
    str_table.insert(GameObjectStr('30', "Tank"))
    str_table.insert(GameObjectStr('16', "AI"))
    str_table.insert(GameObjectStr('61', "AI 2"))
    str_table.display()

    print("\nFind:")
    str_table.display_item(*str_table.find('30'))
    str_table.display_item(*str_table.find('61'))

    print("\nDelete and display:")
    str_table.delete('8')
    str_table.delete('61')
    str_table.display()
