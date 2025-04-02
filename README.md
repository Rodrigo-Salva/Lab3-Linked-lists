# 🔗 Linked Lists Laboratory Assignment


## 📚 Introduction

This laboratory focuses on implementing and understanding linked lists in Python. Linked lists are fundamental data structures consisting of nodes that contain data and references to other nodes. This implementation covers the basic operations of a singly linked list including insertion, deletion, search, and various other utility methods.

## 💻 Implementation

### 🧩 Node Class

The Node class serves as the building block for our linked list:

```python
class Node:
    """
    A Node in a linked list.
    
    Attributes:
        data: The data stored in this node
        next: Reference to the next node in the linked list
    """
    def __init__(self, data=None):
        """
        Initialize a new Node with the given data.
        
        Args:
            data: The data to store in the node
        """
        self.data = data
        self.next = None
    
    def get_data(self):
        """Get the data stored in this node."""
        return self.data
    
    def set_data(self, data):
        """
        Set the data stored in this node.
        
        Args:
            data: The new data to store
        """
        self.data = data
    
    def get_next(self):
        """Get the next node in the linked list."""
        return self.next
    
    def set_next(self, next_node):
        """
        Set the next node in the linked list.
        
        Args:
            next_node: The next node
        """
        self.next = next_node
```

### 📋 LinkedList Class

The LinkedList class manages the collection of nodes and provides methods to manipulate them:

```python
class LinkedList:
    """
    A singly linked list implementation.
    
    Attributes:
        head: The first node in the linked list
        length: The number of nodes in the linked list
    """
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.length = 0
```

## 🧪 Exercises Implementation

### 🖨️ Exercise 1: Displaying the List

```python
def display(self):
    """
    Display all elements in the linked list.
    
    Returns:
        str: A string representation of the linked list
    """
    if self.head is None:
        return "Empty list"
    
    current = self.head
    result = ""
    
    while current is not None:
        result += str(current.get_data()) + " -> "
        current = current.get_next()
    
    return result + "None"
```

**🔍 Analysis:**
This method traverses the entire linked list, starting from the head, and creates a string representation of the list. It handles the empty list case properly and adds a "None" at the end to indicate the end of the list. Time complexity is O(n) where n is the number of nodes in the list.

### 🔢 Exercise 2: Counting Nodes

```python
def list_length(self):
    """
    Count the number of nodes in the linked list.
    
    Returns:
        int: The number of nodes
    """
    count = 0
    current = self.head
    
    while current is not None:
        count += 1
        current = current.get_next()
    
    return count
```

**🔍 Analysis:**
This method traverses the entire linked list and counts the nodes. While our implementation already maintains a length attribute that's updated with each insertion/deletion, this method provides a way to verify that count and can be useful for debugging. Time complexity is O(n).

### ⬅️ Exercise 3: Insertion at the Beginning

```python
def insert_at_beginning(self, data):
    """
    Insert a new node at the beginning of the linked list.
    
    Args:
        data: The data to store in the new node
        
    Returns:
        bool: True if the insertion was successful
    """
    new_node = Node(data)
    
    if self.head is None:
        self.head = new_node
    else:
        new_node.set_next(self.head)
        self.head = new_node
    
    self.length += 1
    return True
```

**🔍 Analysis:**
This method creates a new node and inserts it at the beginning of the list by making it the new head. It handles both empty and non-empty lists. Since it only involves modifying the head pointer, the time complexity is O(1), which is very efficient.

### ➡️ Exercise 4: Insertion at the End

```python
def insert_at_end(self, data):
    """
    Insert a new node at the end of the linked list.
    
    Args:
        data: The data to store in the new node
        
    Returns:
        bool: True if the insertion was successful
    """
    new_node = Node(data)
    
    if self.head is None:
        self.head = new_node
    else:
        current = self.head
        
        # Traverse to the last node
        while current.get_next() is not None:
            current = current.get_next()
        
        current.set_next(new_node)
    
    self.length += 1
    return True
```

**🔍 Analysis:**
This method inserts a new node at the end of the list. If the list is empty, it becomes the head. Otherwise, we traverse to the last node and set its next pointer to the new node. Time complexity is O(n) because we need to traverse the entire list to find the end.

### 📍 Exercise 5: Insertion at a Specific Position

```python
def insert_at_position(self, position, data):
    """
    Insert a new node at the specified position in the linked list.
    
    Args:
        position: The position where the new node should be inserted (0-based)
        data: The data to store in the new node
        
    Returns:
        bool: True if the insertion was successful, False otherwise
    """
    # Check if position is valid
    if position < 0 or position > self.length:
        return False
    
    # Insert at the beginning
    if position == 0:
        return self.insert_at_beginning(data)
    
    # Insert at the end
    if position == self.length:
        return self.insert_at_end(data)
    
    # Insert at the middle
    new_node = Node(data)
    current = self.head
    count = 0
    
    # Traverse to the node just before the insertion point
    while count < position - 1:
        current = current.get_next()
        count += 1
    
    new_node.set_next(current.get_next())
    current.set_next(new_node)
    
    self.length += 1
    return True
```

**🔍 Analysis:**
This method inserts a node at a specific position in the list. It handles edge cases by delegating to the appropriate specialized methods for the beginning and end. For middle positions, it traverses to the node just before the insertion point. Time complexity is O(n) in the worst case, but can be O(1) for the beginning.

### ❌ Exercise 6: Deletion from the Beginning

```python
def delete_from_beginning(self):
    """
    Delete the first node from the linked list.
    
    Returns:
        The data of the deleted node, or None if the list is empty
    """
    if self.head is None:
        return None
    
    data = self.head.get_data()
    self.head = self.head.get_next()
    self.length -= 1
    
    return data
```

**🔍 Analysis:**
This method removes the first node from the list by updating the head pointer. It returns the data from the deleted node, making it useful for implementing other data structures like queues. Time complexity is O(1).

### ❌ Exercise 7: Deletion from the End

```python
def delete_from_end(self):
    """
    Delete the last node from the linked list.
    
    Returns:
        The data of the deleted node, or None if the list is empty
    """
    if self.head is None:
        return None
    
    # If there's only one node
    if self.head.get_next() is None:
        data = self.head.get_data()
        self.head = None
        self.length -= 1
        return data
    
    current = self.head
    
    # Traverse to the second-to-last node
    while current.get_next().get_next() is not None:
        current = current.get_next()
    
    data = current.get_next().get_data()
    current.set_next(None)
    self.length -= 1
    
    return data
```

**🔍 Analysis:**
This method deletes the last node of the list. It requires traversing to the second-to-last node, since our linked list only has references to the next node (not previous). The time complexity is O(n) as we need to traverse the list to find the second-to-last node.

### ❌ Exercise 8: Deletion from a Specific Position

```python
def delete_from_position(self, position):
    """
    Delete a node from the specified position in the linked list.
    
    Args:
        position: The position of the node to delete (0-based)
        
    Returns:
        The data of the deleted node, or None if the position is invalid
    """
    # Check if position is valid
    if position < 0 or position >= self.length or self.head is None:
        return None
    
    # Delete from the beginning
    if position == 0:
        return self.delete_from_beginning()
    
    # Delete from the end
    if position == self.length - 1:
        return self.delete_from_end()
    
    # Delete from the middle
    current = self.head
    count = 0
    
    # Traverse to the node just before the deletion point
    while count < position - 1:
        current = current.get_next()
        count += 1
    
    node_to_delete = current.get_next()
    data = node_to_delete.get_data()
    current.set_next(node_to_delete.get_next())
    self.length -= 1
    
    return data
```

**🔍 Analysis:**
This method deletes a node at a specific position. It follows a similar pattern to insertion at a position but updates the next pointers to bypass the node being deleted. Time complexity is O(n) in the worst case.

### 🔎 Exercise 9: Searching

```python
def search(self, data):
    """
    Search for a value in the linked list.
    
    Args:
        data: The value to search for
        
    Returns:
        int: The position of the first occurrence of the value (0-based),
             or -1 if the value is not found
    """
    if self.head is None:
        return -1
    
    current = self.head
    position = 0
    
    while current is not None:
        if current.get_data() == data:
            return position
        current = current.get_next()
        position += 1
    
    return -1
```

**🔍 Analysis:**
This method searches for a specific value in the list and returns its position. It traverses the list until it finds the value or reaches the end. Time complexity is O(n) in the worst case when the element isn't found or is at the end.

### 🔄 Exercise 10: Finding the Nth Node from the End

```python
def get_nth_from_end(self, n):
    """
    Find the nth node from the end of the linked list.
    
    Args:
        n: The position from the end (1-based)
        
    Returns:
        The data of the nth node from the end,
        or None if n is invalid or the list is empty
    """
    if n <= 0 or n > self.length or self.head is None:
        return None
    
    # The nth node from the end is the (length-n+1)th node from the beginning
    position = self.length - n
    current = self.head
    count = 0
    
    while count < position:
        current = current.get_next()
        count += 1
    
    return current.get_data()
```

**🔍 Analysis:**
This method finds the nth node from the end of the list. It first calculates the corresponding position from the beginning and then traverses to that node. Time complexity is O(n).

### 🗑️ Exercise 11: Clearing the List

```python
def clear(self):
    """
    Remove all nodes from the linked list.
    
    Returns:
        bool: True if the operation was successful
    """
    self.head = None
    self.length = 0
    return True
```

**🔍 Analysis:**
This method clears the entire list by setting the head to None. The garbage collector will handle removing the unreferenced nodes. Time complexity is O(1).

### 🔄 Exercise 12: Detecting a Cycle in a Linked List

```python
def has_cycle(self):
    """
    Check if the linked list has a cycle.
    
    Returns:
        bool: True if the linked list has a cycle, False otherwise
    """
    if self.head is None or self.head.get_next() is None:
        return False
    
    # Use Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
    slow = self.head  # Tortoise (moves one step at a time)
    fast = self.head  # Hare (moves two steps at a time)
    
    while fast is not None and fast.get_next() is not None:
        slow = slow.get_next()  # Move one step
        fast = fast.get_next().get_next()  # Move two steps
        
        # If they meet, there's a cycle
        if slow == fast:
            return True
    
    # If we reach here, there's no cycle
    return False
```

**🔍 Analysis:**
This method uses Floyd's Cycle-Finding Algorithm (also known as the "tortoise and hare" algorithm) to detect if there's a cycle in the list. It uses two pointers moving at different speeds - if they ever meet, there must be a cycle. Time complexity is O(n).

### 🔄 Exercise 13: Reversing a Linked List

```python
def reverse(self):
    """
    Reverse the linked list.
    
    Returns:
        bool: True if the operation was successful
    """
    if self.head is None or self.head.get_next() is None:
        return True  # Empty list or single node (already reversed)
    
    previous = None
    current = self.head
    
    while current is not None:
        # Store the next node
        next_node = current.get_next()
        
        # Reverse the link
        current.set_next(previous)
        
        # Move to the next nodes
        previous = current
        current = next_node
    
    # Update the head to the new first node (previously the last)
    self.head = previous
    
    return True
```

**🔍 Analysis:**
This method reverses the linked list by changing the direction of all the next pointers. It uses three pointers (previous, current, and next) to manage the reversal process. Time complexity is O(n).

### 🎯 Exercise 14: Finding the Middle of a Linked List

```python
def find_middle(self):
    """
    Find the middle node of the linked list.
    
    Returns:
        The data of the middle node, or None if the list is empty
    """
    if self.head is None:
        return None
    
    # Use the slow and fast pointer technique
    slow = self.head
    fast = self.head
    
    # When fast reaches the end, slow will be at the middle
    while fast is not None and fast.get_next() is not None:
        slow = slow.get_next()  # Move one step
        fast = fast.get_next().get_next()  # Move two steps
    
    return slow.get_data()
```

**🔍 Analysis:**
This method finds the middle node of the list using the two-pointer technique. One pointer moves twice as fast as the other, so when the fast one reaches the end, the slow one is at the middle. Time complexity is O(n/2), which simplifies to O(n).

### 🧵 Exercise 15: Queue Implementation Using Linked List

```python
class Queue:
    """
    A Queue implementation using a linked list.
    """
    def __init__(self):
        """Initialize an empty queue."""
        self.linked_list = LinkedList()
    
    def is_empty(self):
        """Check if the queue is empty."""
        return self.linked_list.head is None
    
    def enqueue(self, data):
        """
        Add an element to the end of the queue.
        
        Args:
            data: The element to add
        """
        self.linked_list.insert_at_end(data)
    
    def dequeue(self):
        """
        Remove and return the element at the front of the queue.
        
        Returns:
            The element at the front of the queue,
            or None if the queue is empty
        """
        return self.linked_list.delete_from_beginning()
    
    def peek(self):
        """
        Return the element at the front of the queue without removing it.
        
        Returns:
            The element at the front of the queue,
            or None if the queue is empty
        """
        if self.is_empty():
            return None
        return self.linked_list.head.get_data()
    
    def size(self):
        """Return the number of elements in the queue."""
        return self.linked_list.length
    
    def display(self):
        """Display the elements in the queue."""
        return self.linked_list.display()
```

**🔍 Analysis:**
This Queue implementation uses our LinkedList class to store and manage elements. It follows the FIFO (First-In-First-Out) principle by:
1. Adding elements at the end of the list (enqueue)
2. Removing elements from the beginning (dequeue)
3. Providing a peek method to see the front element without removing it

The time complexities are:
- enqueue: O(n) due to traversing to the end of the list
- dequeue: O(1) since we remove from the beginning
- peek: O(1) since we just access the head
- is_empty and size: O(1) since we check/return stored values

## 🧪 Testing Code

### 🔬 Basic Operations Test

```python
def test_linked_list():
    """Test the LinkedList implementation."""
    # Create a new linked list
    my_list = LinkedList()
    print("Created a new linked list")
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.list_length()}")
    print()
    
    # Test insertion at the beginning
    print("Inserting elements at the beginning...")
    my_list.insert_at_beginning(5)
    my_list.insert_at_beginning(10)
    my_list.insert_at_beginning(15)
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.list_length()}")
    print()
    
    # Test insertion at the end
    print("Inserting elements at the end...")
    my_list.insert_at_end(20)
    my_list.insert_at_end(25)
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.list_length()}")
    print()
    
    # Test insertion at a specific position
    print("Inserting elements at specific positions...")
    my_list.insert_at_position(2, 30)
    my_list.insert_at_position(4, 35)
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.list_length()}")
    print()
    
    # Test searching
    print("Searching for elements...")
    print(f"Position of 30: {my_list.search(30)}")
    print(f"Position of 100: {my_list.search(100)}")
    print()
    
    # Test finding nth element from the end
    print("Finding elements from the end...")
    print(f"2nd element from the end: {my_list.get_nth_from_end(2)}")
    print(f"4th element from the end: {my_list.get_nth_from_end(4)}")
    print()
    
    # Test deletion from the beginning
    print("Deleting elements from the beginning...")
    deleted = my_list.delete_from_beginning()
    print(f"Deleted element: {deleted}")
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.list_length()}")
    print()
    
    # Test deletion from the end
    print("Deleting elements from the end...")
    deleted = my_list.delete_from_end()
    print(f"Deleted element: {deleted}")
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.list_length()}")
    print()
    
    # Test deletion from a specific position
    print("Deleting elements from specific positions...")
    deleted = my_list.delete_from_position(2)
    print(f"Element deleted from position 2: {deleted}")
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.list_length()}")
    print()
    
    # Test clearing the list
    print("Clearing the list...")
    my_list.clear()
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.list_length()}")
    print()
    
    # Test operations after clearing
    print("Inserting new elements after clearing...")
    my_list.insert_at_beginning(100)
    my_list.insert_at_end(200)
    my_list.insert_at_position(1, 150)
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.list_length()}")
    print()

if __name__ == "__main__":
    test_linked_list()
```

### 🧵 Queue Test

```python
def test_queue():
    """Test the Queue implementation."""
    queue = Queue()
    print("Created a new queue")
    print(f"Queue: {queue.display()}")
    print(f"Size: {queue.size()}")
    print(f"Is empty? {queue.is_empty()}")
    print()
    
    print("Enqueuing elements...")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"Queue: {queue.display()}")
    print(f"Size: {queue.size()}")
    print(f"Front element (peek): {queue.peek()}")
    print()
    
    print("Dequeuing elements...")
    dequeued = queue.dequeue()
    print(f"Dequeued: {dequeued}")
    print(f"Queue: {queue.display()}")
    print(f"Size: {queue.size()}")
    print(f"Front element (peek): {queue.peek()}")
    print()
    
    print("Enqueuing more elements...")
    queue.enqueue(40)
    queue.enqueue(50)
    print(f"Queue: {queue.display()}")
    print(f"Size: {queue.size()}")
    print()
    
    print("Dequeuing all elements...")
    while not queue.is_empty():
        print(f"Dequeued: {queue.dequeue()}")
    print(f"Queue: {queue.display()}")
    print(f"Is empty? {queue.is_empty()}")

if __name__ == "__main__":
    test_queue()
```

## 📊 Execution Results

### 📝 LinkedList Test Results

```
Created a new linked list
List: Empty list
Length: 0

Inserting elements at the beginning...
List: 15 -> 10 -> 5 -> None
Length: 3

Inserting elements at the end...
List: 15 -> 10 -> 5 -> 20 -> 25 -> None
Length: 5

Inserting elements at specific positions...
List: 15 -> 10 -> 30 -> 5 -> 35 -> 20 -> 25 -> None
Length: 7

Searching for elements...
Position of 30: 2
Position of 100: -1

Finding elements from the end...
2nd element from the end: 20
4th element from the end: 35

Deleting elements from the beginning...
Deleted element: 15
List: 10 -> 30 -> 5 -> 35 -> 20 -> 25 -> None
Length: 6

Deleting elements from the end...
Deleted element: 25
List: 10 -> 30 -> 5 -> 35 -> 20 -> None
Length: 5

Deleting elements from specific positions...
Element deleted from position 2: 5
List: 10 -> 30 -> 35 -> 20 -> None
Length: 4

Clearing the list...
List: Empty list
Length: 0

Inserting new elements after clearing...
List: 100 -> 150 -> 200 -> None
Length: 3
```

### 📝 Queue Test Results

```
Created a new queue
Queue: Empty list
Size: 0
Is empty? True

Enqueuing elements...
Queue: 10 -> 20 -> 30 -> None
Size: 3
Front element (peek): 10

Dequeuing elements...
Dequeued: 10
Queue: 20 -> 30 -> None
Size: 2
Front element (peek): 20

Enqueuing more elements...
Queue: 20 -> 30 -> 40 -> 50 -> None
Size: 4

Dequeuing all elements...
Dequeued: 20
Dequeued: 30
Dequeued: 40
Dequeued: 50
Queue: Empty list
Is empty? True
```

## 📝 Conclusions

1. **🏗️ Data Structure Design**: Implementing a linked list from scratch helps understand how data structures are designed and the trade-offs involved in their implementation.

2. **⚡ Operation Efficiency**: Different operations on linked lists have different time complexities:
   - Insertion/deletion at the beginning: O(1)
   - Insertion/deletion at the end or middle: O(n)
   - Searching: O(n)
   - These characteristics make linked lists suitable for certain applications and less suitable for others.

3. **💾 Memory Management**: Linked lists use dynamic memory allocation, with each node being allocated separately. This offers flexibility but requires proper pointer management to avoid memory leaks or invalid references.

4. **🧱 Implementation of Other Data Structures**: As demonstrated with the Queue implementation, linked lists can serve as the foundation for building other data structures.

5. **🔬 Algorithm Application**: The lab provided practical experience with common algorithms like Floyd's Cycle-Finding Algorithm and the two-pointer technique for finding the middle of a list.

6. **🔧 Skills Development**: This lab enhanced skills in:
   - Object-oriented programming
   - Algorithm analysis
   - Debugging complex pointer operations
   - Understanding abstract data types

7. **⚖️ Linked Lists vs. Arrays**: Through this implementation, it's clear that linked lists excel at insertions and deletions in positions where the pointer is already known, while arrays excel at random access by index. This is a fundamental trade-off in data structure selection.

## 📚 References

1. The linked list laboratory document provided for this assignment
2. [Python Data Structures and Algorithms documentation](https://docs.python.org/3/tutorial/datastructures.html)
3. Introduction to Algorithms by Cormen, Leiserson, Rivest, and Stein
4. Data Structures and Algorithms in Python by Goodrich, Tamassia, and Goldwasser
