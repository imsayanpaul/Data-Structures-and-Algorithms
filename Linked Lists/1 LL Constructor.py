# Create a singly linked list with one node containing the value 4.

# Your implementation should:

# Create a Node class where each node has:
# value
# next

# Create a LinkedList class that keeps track of:
# head
# tail
# length

# Create a linked list with the value 4.
# Print the head value, tail value, and length.

#     EXPECTED OUTPUT:
#     ----------------
#     Head: 4
#     Tail: 4
#     Length: 1



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1



 
my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


