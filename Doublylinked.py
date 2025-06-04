#  doubly linked list

class Node:
    data = None
    nextNode = None
    prevNode = None

    def __init__(self, value):
        self.data = value
        self.nextNode = None
        self.prevNode = None


head = None
n = int(input("Enter the number of nodes : "))
for _ in range(n):
    newNode = Node(input("Enter the node data : "))
    if head == None:
        head = newNode
        currentNode = head
    else:
        currentNode.nextNode = newNode
        newNode.prevNode = currentNode
        currentNode = newNode
temp = head
temp1 = None
while (temp != None):
    print(temp.data, end='')
    temp1 = temp
    temp = temp.nextNode
print()
while (temp1 != None):
    print(temp1.data, end='')
    temp1 = temp1.prevNode
print()
