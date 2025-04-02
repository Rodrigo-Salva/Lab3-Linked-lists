class Node:
    """Representa un nodo en una lista enlazada."""
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

class LinkedList:
    """Implementación de una lista enlazada."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_at_end(self, data):
        """Inserta un elemento al final de la lista."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def delete_from_beginning(self):
        """Elimina y devuelve el primer elemento de la lista."""
        if self.head is None:
            return None
        removed_data = self.head.get_data()
        self.head = self.head.next
        if self.head is None:
            self.tail = None  # Si la lista queda vacía
        self.length -= 1
        return removed_data

    def display(self):
        """Devuelve una representación en cadena de la lista enlazada."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.get_data()))
            current = current.next
        return " -> ".join(elements) if elements else "Queue is empty"

class Queue:
    """Implementación de una cola usando una lista enlazada."""
    def __init__(self):
        self.linked_list = LinkedList()
    
    def is_empty(self):
        return self.linked_list.head is None
    
    def enqueue(self, data):
        self.linked_list.insert_at_end(data)
    
    def dequeue(self):
        return self.linked_list.delete_from_beginning()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.linked_list.head.get_data()
    
    def size(self):
        return self.linked_list.length
    
    def display(self):
        return self.linked_list.display()

def test_queue():
    """Prueba la implementación de la cola."""
    queue = Queue()
    print("Creando una nueva cola")
    print(f"Cola: {queue.display()}")
    print(f"Tamaño: {queue.size()}")
    print(f"¿Está vacía? {queue.is_empty()}")
    print()
    
    print("Encolando elementos...")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"Cola: {queue.display()}")
    print(f"Tamaño: {queue.size()}")
    print(f"Elemento frontal (peek): {queue.peek()}")
    print()
    
    print("Desencolando elementos...")
    dequeued = queue.dequeue()
    print(f"Desencolado: {dequeued}")
    print(f"Cola: {queue.display()}")
    print(f"Tamaño: {queue.size()}")
    print(f"Elemento frontal (peek): {queue.peek()}")
    print()
    
    print("Encolando más elementos...")
    queue.enqueue(40)
    queue.enqueue(50)
    print(f"Cola: {queue.display()}")
    print(f"Tamaño: {queue.size()}")
    print()
    
    print("Desencolando todos los elementos...")
    while not queue.is_empty():
        print(f"Desencolado: {queue.dequeue()}")
    print(f"Cola: {queue.display()}")
    print(f"¿Está vacía? {queue.is_empty()}")

if __name__ == "__main__":
    test_queue()
