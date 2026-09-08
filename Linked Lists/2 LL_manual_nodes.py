# Create a singly linked list containing the values 4, 10, 20, and 30.

# Your linked list should:

# Create a Node class with value and next.
# Create a LinkedList class with:
# head
# tail
# length
# Connect the nodes so the list looks like:
# 4 → 10 → 20 → 30 → None

# Finally, print:

# Head: 4
# Tail: 30
# Length: 4

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


# Create linked list with first value
my_linked_list = LinkedList(4)
# Create 3 more nodes
node2 = Node(10)
node3 = Node(20)
node4 = Node(30)


# Connect the nodes
my_linked_list.head.next = node2
node2.next = node3
node3.next = node4
my_linked_list.tail = node4

my_linked_list.length = 4

print('Head is', my_linked_list.head.value)
print('Tail is', my_linked_list.tail.value)
print('Length is', my_linked_list.length)