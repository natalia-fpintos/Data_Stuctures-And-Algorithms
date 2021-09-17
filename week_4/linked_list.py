class Link:
    def __init__(self, data):
        self.data = data
        self.next = None

    def display(self):
        print(self.data)

    def get_data(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.first = None

    def display(self):
        current = self.first

        while current is not None:
            current.display()
            current = current.next

    def is_empty(self):
        return self.first is None

    def insert(self, new_link):
        new_link.next = self.first
        self.first = new_link

    def delete(self, key):
        to_delete, previous = self.find(key)
        if to_delete is None:
            return False
        if to_delete == previous:
            self.first = to_delete.next
            return True
        previous.next = to_delete.next
        return True

    def delete_first(self):
        self.first = self.first.next
        return True

    def find(self, key):
        current = self.first
        previous = self.first
        while current is not None:
            if current.data == key:
                return current, previous
            previous = current
            current = current.next
        return None, None


if __name__ == "__main__":
    linked_list = LinkedList()
    links = [Link('1'), Link('2'), Link('3'), Link('4'), Link('5'), Link('6')]

    for link in links:
        linked_list.insert(link)

    linked_list.display()

    for i in ['4', '8']:
        found = linked_list.find(i)
        if found is not None:
            print(f"Item {i} found")
        else:
            print(f"Item {i} not found")

    for i in ['4', '8']:
        deleted = linked_list.delete(i)
        if deleted:
            print(f"Item {i} deleted")
            linked_list.display()
        else:
            print(f"Item {i} could not be deleted")
            linked_list.display()

    deleted_first = linked_list.delete_first()

    if deleted_first:
        print(f"First item deleted")
        linked_list.display()
