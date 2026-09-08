class Node:  # create Node
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:  # create LinkedList
    def __init__(self, value):
        New_Node = Node(value)
        self.head = New_Node
        self.tail = New_Node
        self.length = 1

    def append(self, value):  # append
        New_Node = Node(value)
        if self.length == 0:
            self.head = New_Node
            self.tail = New_Node
        else:
            self.tail.next = New_Node
            self.tail = New_Node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0: # Return None when the list is empty because there is no node to remove.
            return None

        temp = self.head
        pre = self.head

        # Move through the list while keeping pre one node behind temp
        while temp.next:
            pre = temp
            temp = temp.next

        # and decrease the linked list length
        self.tail = pre  # Make the previous node the new tail
        self.tail.next = None  # disconnect the old tail
        self.length -= 1  # and decrease the linked list length

        if self.length == 0:  # If the last node was removed, the list is now empty,
            self.head = None  # so set both head and tail to None
            self.tail = None

        return temp  # Return the removed node.

    def Print_list(self):  # Print Linked List
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


New_linkedList = LinkedList(10)
New_linkedList.append(20)
New_linkedList.append(30)

New_linkedList.pop()




print("Head:", New_linkedList.head.value)
print("Tail:", New_linkedList.tail.value)
print("Length:", New_linkedList.length)
New_linkedList.Print_list()
