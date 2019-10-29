class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self, head):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def search(self, data):
        index = 0
        found = False
        current = self.head
        while found==False:
            if(current.get_data()==data):
                found = True
            else :
                current = current.get_next()
            index+=1
        
        return str(data)+" found at index "+str(index)

head_node = Node("a")
llist = LinkedList(head_node)
llist.insert("b")
llist.insert("c")
llist.insert("d")
llist.insert("e")
llist.insert("f")
llist.insert("g")
llist.insert("h")
llist.insert("i")

print(llist.search("f"))