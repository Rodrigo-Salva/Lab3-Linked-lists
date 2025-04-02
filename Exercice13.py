class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        result = ""
        while current:
            result += f"[{current.data}] -> "
            current = current.next
        return result + "None"

    def reverse(self):
        previous, current = None, self.head
        while current:
            next_node = current.next
            current.next = previous
            previous, current = current, next_node
        self.head = previous


# Pruebas
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)
    
    print("Lista Original:")
    print(linked_list.display())
    
    linked_list.reverse()
    
    print("\nLista Invertida:")
    print(linked_list.display())
