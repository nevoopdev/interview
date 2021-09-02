class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    
    def push(self ,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
    
    def print(self):
        temp = self.head

        while(temp):
            print(temp.data)
            temp = temp.next
    def reverse(self):
        prev = None
        current = self.head
        while(current!=None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


ll = LinkedList()

ll.push(1)
ll.push(2)
ll.push(3)

ll.print()
ll.reverse()
print("after reverse")
ll.print()


    
    

