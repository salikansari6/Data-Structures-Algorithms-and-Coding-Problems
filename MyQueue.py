# class Queue:
#     def __init__(self):
#         self.first = None
#         self.last = None
#         self.length = 0
#
#     def enqueue(self,value):
#         node = Node(value)
#         if self.length == 0:
#             self.first = node
#             self.last = node
#         else:
#             temp = self.last
#             temp.next = node
#             self.last = node
#         self.length += 1
#
#     def dequeue(self):
#         if self.length == 0:
#             return None
#         temp = self.first
#         if self.length == 1:
#             self.first = None
#             self.last = None
#             self.length -= 1
#         else:
#             self.first = self.first.next
#             self.length -= 1
#         return temp
#
#     def print(self):
#         temp = self.first
#         while temp is not None:
#             print(temp.value, end=" ")
#             temp = temp.next
#
#
# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
#
#
# queue = Queue()
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# queue.enqueue(40)
# queue.enqueue(50)
# queue.dequeue()
# queue.print()
