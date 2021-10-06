from random import randint


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def display(self):
        print(self.data)
        
    @property
    def is_leaf(self):
        return self.left_child is None and self.right_child is None
    
    @property
    def has_left_child(self):
        return self.left_child is not None
        
    @property
    def has_right_child(self):
        return self.right_child is not None
    
    @property
    def has_one_child(self):
        return (self.left_child is None and self.has_right_child) or (self.has_left_child and self.right_child is None)

    @property
    def has_two_children(self):
        return self.has_left_child and self.has_right_child
        
    def find_smallest_and_parent(self, local_root):
        smallest = local_root
        parent = local_root
        while smallest.has_left_child:
            parent = smallest
            smallest = smallest.left_child
        return smallest, parent
    
    @property
    def successor_info(self):
        return self.find_smallest_and_parent(self.right_child)


class Tree:
    def __init__(self):
        self.root = None
        

    def find(self, key):
        current = self.root
        parent = self.root
        while current.data != key:
            parent = current
            if key < current.data:
                current = current.left_child
            else:
                current = current.right_child

            if current is None:
                return None
        return (current, parent)

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
    
                        
    def delete(self, key):
        node, parent = self.find(key)
        if node.is_leaf:
            # Node is a leaf, we can remove its ref from the parent
            if node == self.root:
                self.root = None
            elif parent.left_child.data == node.data:
                parent.left_child = None
            else:
                parent.right_child = None
        elif node.has_one_child:
            # Node has one child, we can replace the deleted node with it
            child = node.left_child if node.has_left_child else node.right_child
            if node == self.root:
                self.root = child
            elif parent.left_child.data == node.data:
                parent.left_child = child
            else:
                parent.right_child = child
        else:
            # Node has two children, we need to replace with next successor
            successor, s_parent = node.successor_info
            s_right_tree = successor.right_child
            successor.left_child = node.left_child
            successor.right_child = node.right_child
            s_parent.left_child = s_right_tree
            
            if node == self.root:
                self.root = successor
            elif parent.left_child.data == node.data:
                parent.left_child = successor
            else:
                parent.right_child = successor
        


if __name__ == "__main__":
    tree = Tree()

    for _ in range(6):
        tree.insert(randint(1, 100))

    tree.display_in_order(tree.root)
    
    tree_2 = Tree()
    
    for i in [5, 2, 8, 4, 9, 1, 6, 3, 7]:
        tree_2.insert(i)
    
    tree_2.display_in_order(tree_2.root)
    
    tree_2.delete(3)
    tree_2.delete(1)
    
    tree_2.display_in_order(tree_2.root)
    
    tree_2.delete(2)
    
    tree_2.display_in_order(tree_2.root)
    
    tree_2.delete(5)
    
    tree_2.display_in_order(tree_2.root)
