from random import randint


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def display(self):
        print(self.data)


class Tree:
    def __init__(self):
        self.root = None

    def find(self, key):
        current = self.root
        while current.data != key:
            if key < current.data:
                current = current.left_child
            else:
                current = current.right_child

            if current is None:
                return None
        return current

    def display_in_order(self, local_root):
        if local_root is not None:
            self.display_in_order(local_root.left_child)
            local_root.display()
            self.display_in_order(local_root.right_child)

    def less_than(self, new_node, existing_node):
        return new_node.data < existing_node.data

    def _create_tree_node(self, *args, **kwargs):
        return Node(*args)
        
    def insert(self, *args, **kwargs):
        new_node = self._create_tree_node(*args)

        if self.root is None:
            # Tree is empty
            self.root = new_node
        else:
            # Start at the root
            current = self.root
            while True:
                # Keep track of the current node as a "parent" for the new node
                parent = current
                if self.less_than(new_node, current):
                    # The new node is smaller than the current node, we move left
                    current = current.left_child
                    if current is None:
                        # The left is empty, we can add the new node
                        parent.left_child = new_node
                        return
                else:
                    # The new node is greater or equal than the current node, we move right
                    current = current.right_child
                    if current is None:
                        # The right is empty, we can add the new node
                        parent.right_child = new_node
                        return


if __name__ == "__main__":
    tree = Tree()

    for _ in range(6):
        tree.insert(randint(1, 100))

    tree.display_in_order(tree.root)
