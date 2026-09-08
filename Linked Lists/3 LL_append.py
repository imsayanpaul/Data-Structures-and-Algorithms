class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        New_node = Node(value)
        self.head = New_node
        self.tail = New_node
        self.length = 1

    def append(self, value):
        New_node = Node(value)
        if self.length == 0:
            self.head = New_node
            self.tail = New_node
        else:
            self.tail.next = New_node
            self.tail = New_node
        self.length += 1
        return True
    

    def Print_lines(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


New_linked_list = LinkedList(10)

New_linked_list.append(20)
New_linked_list.append(30)
New_linked_list.append(40)
New_linked_list.append(50)

print("\nAfter append:")
print("head:", New_linked_list.head.value)
print("Tail:", New_linked_list.tail.value)
print("Length:", New_linked_list.length)

print("\nList:")
New_linked_list.Print_lines()
