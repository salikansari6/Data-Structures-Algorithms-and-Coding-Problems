class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def shift(self):
        if self.head is None:
            print("List is empty")
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            shifted = self.head
            self.head = shifted.next
            self.head.prev = None
            shifted.next = None
        self.length -= 1
        return shifted

    def get(self, index):
        if index == self.length - 1:
            return self.tail
        if index == 0:
            return self.head
        if index >= self.length // 2:
            count = self.length - 1
            ptr = self.tail
            while count != index:
                ptr = ptr.prev
                count -= 1
            return ptr
        else:
            count = 0
            ptr = self.head
            while count != index:
                ptr = ptr.next
                count += 1
            return ptr

    def set(self, index, value):
        foundNode = self.get(index)
        if foundNode is not None:
            foundNode.value = value
        else:
            return False


    def push(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def insert(self, index, value):
        ptr = self.head
        newNode = Node(value)
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.unshift(value)
        elif index == self.length - 1:
            return self.push(value)
        prevNode = self.get(index-1)
        newNode.next = prevNode.next
        newNode.next.prev = newNode
        prevNode.next = newNode
        newNode.prev = prevNode
        self.length +=1

    def remove(self,index):
        if self.head is None:
            print("List is  empty")
            return None
        if index < 0 or index > self.length:
            return False
        if index ==  self.length - 1:
            return self.pop()
        elif index == 0:
            return self.unshift()
        else:
            prevNode = self.get(index - 1)
            to_be_removed = prevNode.next
            to_be_removed.next.prev = prevNode
            prevNode.next = to_be_removed.next
            self.length -= 1
            return to_be_removed



    def unshift(self,value):
        unshifted = Node(value)
        if self.head is None:
            self.head = unshifted
            self.tail = unshifted
        else:
            self.head.prev = unshifted
            unshifted.next = self.head
            self.head = unshifted
        self.length +=1

    def pop(self):
        if self.head is None:
            print("Linked List is empty")
            return None
        node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            node.prev.next = None
            self.tail = node.prev
            node.prev = None
        self.length -= 1
        return node

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        ptr = self.head
        output = ""
        while ptr:
            output += str(ptr.value) + " <--> "
            ptr = ptr.next
        print(output)


myDoublyLinkedList = DoublyLinkedList()
myDoublyLinkedList.push(18)
myDoublyLinkedList.push(10)
myDoublyLinkedList.push(6)
myDoublyLinkedList.push(5)
myDoublyLinkedList.push(12)
myDoublyLinkedList.push(67)
myDoublyLinkedList.push(21)
myDoublyLinkedList.push(98)
myDoublyLinkedList.unshift(69)
myDoublyLinkedList.set(1,765)
myDoublyLinkedList.insert(1,321)
myDoublyLinkedList.remove(2)



myDoublyLinkedList.print_list()
