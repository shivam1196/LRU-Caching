from caching.node.HashNode import HashNode


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def enter_value(self, key, value):
        if self.head is None:
            self.head = HashNode(key, value)
            self.head.next = None
            self.head.prev = None
            self.tail = self.head
            return self.head

        else:
            temp = HashNode(key,value)
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = self.tail.next
            return temp

    def access_a_node(self, node):
        temp_node = node
        if temp_node.prev is None:
            self.tail.next = temp_node
            self.tail = self.tail.next
            self.head = self.head.next
            self.head.prev = None

        else:
            temp_prev_node = temp_node.prev
            temp_next_node = temp_node.next  # type: HashNode
            temp_prev_node.next = temp_next_node
            temp_next_node.prev = temp_prev_node
            temp_node.next = None
            self.tail.next = temp_node
            self.tail = self.tail.next

    def replace_a_node(self, key, value):
        temp_node = HashNode(key, value)
        self.tail.next = temp_node
        self.tail = self.tail.next
        self.head = self.head.next
        self.head.prev = None
        return temp_node

    def get_head_node(self):
        return self.head

    def print_doubly_linked_list(self):
        temp = self.head
        while temp is not None:
            print temp.key ," ", temp.value
            temp = temp.next

    def print_doubly_linked_list_reverse(self):
        temp = self.tail

        while temp is not None:
            print temp.key, " " , temp.value
            temp = temp.prev


"""
replace a node when new node comes and cache is full
"""
