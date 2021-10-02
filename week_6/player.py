import random
from tree import Tree


class Player:
    def __init__(self, level, kills):
        self.level = level
        self.kills = kills
        self.left_child = None
        self.right_child = None

    def display(self):
        print(f"Level: {self.level}. Kills: {self.kills}")

    def factorial(self, n):
        if n == 1:
            return 1
        return self.factorial(n-1) * n

    @property
    def score(self):
        return self.factorial(self.level) * self.kills


class PlayerTree(Tree):
    def _create_tree_node(self, *args, **kwargs):
        return Player(*args)
    
    def less_than(self, new_node, existing_node):
        return new_node.score < existing_node.score
        

if __name__ == "__main__":
    player_tree = PlayerTree()
    for _ in range(10):
        level = random.randint(1, 10)
        kills = random.randint(1, 10)
        player_tree.insert(level, kills)
    
    player_tree.display_in_order(player_tree.root)

