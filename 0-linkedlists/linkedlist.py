from node import Node

class Linkedlist:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linkedlist list is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + " --> " if itr.next else str(itr.data)
            itr = itr.next

        print(llstr)
        
    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1

        return count
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head) # check
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)
    
    def insert_at(self, idx, data):
        if idx < 0 or idx > self.get_length():
            raise Exception("Invalid index")
        
        if idx == 0:
            self.insert_at_beginning(data)
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == idx - 1:
                node = Node(data, itr.next, None)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, idx):
        if idx < 0 or idx > self.get_length():
            raise Exception("Invalid index")
        
        if idx == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0

        while itr:
            if count == idx - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


    def print_backwards(self):
        if self.head is None:
            print("Linkedlist list is empty")
            return

        itr = self.get_last_node()
        llstr = ''

        while itr:
            llstr += str(itr.data) + " --> " if itr.prev else str(itr.data)
            itr = itr.prev

        print(llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr