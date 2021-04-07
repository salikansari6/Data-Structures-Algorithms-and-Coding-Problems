class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, value):
        node = Node(value)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            temp = self.first
            self.first = node
            self.first.next = temp
        self.size += 1
        return self.size

    def pop(self):
        if self.first is None:
            return None
        if self.size == 1:
            self.first = None
            self.last = None
        else:
            temp = self.first
            self.first = temp.next
        self.size -= 1
        return temp

    def print_stack(self):
        temp = self.first
        while temp is not None:
            print("|   " + str(temp.value) + "   |")
            print("-----------")
            temp = temp.next




class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
stack.pop()
stack.print_stack()