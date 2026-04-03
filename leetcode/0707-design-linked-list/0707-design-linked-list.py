class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        node = self.head
        for _ in range(index):
            node = node.next
        
        return node.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if not self.head:
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        if index <= 0:
            self.addAtHead(val)
            return
        
        node = self.head
        for _ in range(index - 1):
            node = node.next
        
        new_node = Node(val)
        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.head = self.head.next
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            
            node.next = node.next.next
        
        self.size -= 1