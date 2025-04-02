class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def has_cycle(self):
        """
        Detects if the linked list contains a cycle.

        Returns:
            bool: True if a cycle is detected, False otherwise.
        """
        if self.head is None or self.head.get_next() is None:
            return False

        slow = self.head  # Tortoise (moves one step)
        fast = self.head  # Hare (moves two steps)

        while fast is not None and fast.get_next() is not None:
            slow = slow.get_next()           
            fast = fast.get_next().get_next() 

            if slow == fast:  # Cycle detected
                return True

        return False  # No cycle detected

# Example Usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    linked_list.head = node1
    node1.set_next(node2)
    node2.set_next(node3)
    node3.set_next(node4)
    node4.set_next(node2)  # Creating a cycle

    print(linked_list.has_cycle())  # Output: True
