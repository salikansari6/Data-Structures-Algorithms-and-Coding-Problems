class LinkedList:
    def __init__(self,head):
        node = Node(head,None)
        self.head = node
        self.length = 1

    def insert_at_beginning(self,value):
        node = Node(value,self.head)
        self.head = node
        self.length+=1

    def insert_after_value(self,data_after,data_to_insert):
        ptr = self.head
        while ptr.value!=data_after:
            ptr = ptr.next
        node = Node(data_to_insert,ptr.next)
        ptr.next = node

    def insert_at(self,value,index):
        if(index == self.length):
            self.insert_at_end(value)
            self.length+=1
        if(index == 0):
            self.insert_at_beginning(value)
            self.length+=1
            return
        ptr = self.head
        count = 0
        while ptr:
            if(count == index-1):
                node = Node(value,ptr.next)
                ptr.next = node
                break
            ptr = ptr.next
            count+=1

    def remove_by_value(self,value):
        ptr = self.head
        count = 0
        while ptr.value != value:
            count +=1
            ptr = ptr.next
        self.remove_at(count)

    def remove_at(self,index):
        if(index == 0):
            self.head = self.head.next
            self.length-=1
            return
        ptr = self.head
        count = 0
        while ptr:
            if(count == index-1):
                ptr.next = ptr.next.next
                self.length-=1
                break
            ptr = ptr.next
            count+=1

    def insert_at_end(self,value):
        if self.length==0:
            self.insert_at_beginning(value)
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(value,None)
        self.length+=1

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        ptr = self.head
        output=""
        while ptr:
            output += str(ptr.value) + " --> "
            ptr = ptr.next
        print(output)

class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next

if __name__ == '__main__':
    myLinkedList = LinkedList(10)
    myLinkedList.insert_at_beginning(9)
    myLinkedList.insert_at_beginning(7)
    myLinkedList.insert_at_end(8)
    myLinkedList.remove_at(1)
    myLinkedList.insert_at(5,2)
    myLinkedList.insert_after_value(10,51)
    myLinkedList.remove_by_value(51)

    myLinkedList.print_list()
    print(myLinkedList.length)
