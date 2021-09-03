"""Vectors (lists)"""
from random import randrange


class Weapon:
    def __init__(self, weapon_id=randrange(10)):
        self.id = weapon_id

    def __eq__(self, other):
        return self.id == other


if __name__ == '__main__':
    print("\n---------Iterator for list of weapons---------")
    weapons = [Weapon(i) for i in range(10)]
    it = iter(weapons)
    for w in it:
        print(w.id)

    it2 = iter(weapons)
    weapons.remove(6)  # Equality operator is overloaded to compare id with this

    print([w.id for w in weapons])
