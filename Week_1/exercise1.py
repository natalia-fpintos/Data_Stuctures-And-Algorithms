"""Operator overloading"""


class Entity:
    def __init__(self, s):
        self.size = s

    def __add__(self, other):
        return self.size + other.size

    def __sub__(self, other):
        return self.size - other.size

    def __iadd__(self, other):
        """In-place add - will run for += operations.
        Runs logic but not the assignment: needs to return self or the variable will be assigned None"""
        self.size += other
        return self

    def __isub__(self, other):
        """In-place subtract - will run for -= operations.
        Runs logic but not the assignment: needs to return self or the variable will be assigned None"""
        self.size -= other
        return self

    def __gt__(self, other):
        return self.size > other.size

    def __lt__(self, other):
        return self.size < other.size


if __name__ == '__main__':
    entity1 = Entity(5)
    entity2 = Entity(2)

    print("\n---------Sum/Subtract of entities---------")
    print("Sum of entity1 + entity2: {}".format(entity1 + entity2))
    print("Subtract of entity1 - entity2: {}".format(entity1 - entity2))

    print("\n---------Increment and decrement entities---------")
    entity1 += 1
    print("Increment size of entity1: {}".format(entity1.size))
    entity2 -= 1
    print("Decrement size of entity2: {}".format(entity2.size))

    print("\n---------Comparison of entities---------")
    print("Entity1 is greater than entity2: {}".format(entity1 > entity2))
    print("Entity1 is less than entity2: {}".format(entity1 < entity2))
