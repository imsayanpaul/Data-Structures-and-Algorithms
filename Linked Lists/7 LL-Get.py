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

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        pre = self.head
        temp = self.head

        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def print_List(self):
        temp = self.head
        while temp:
            print (temp.value)
            temp = temp.next

    def prepend(self, value):
            new_node = Node(value)
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node
            self.length += 1
            return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range (index):
            temp = temp.next
        return temp

New_linked_list = LinkedList (10)
New_linked_list.append(20)
New_linked_list.append(30)
# New_linked_list.pop()
New_linked_list.prepend(55)
# pop_var = New_linked_list.pop_first()
New_linked_list.print_List()
print("Length:",New_linked_list.length)
print(New_linked_list.get(0).value)