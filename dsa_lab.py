class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node('Buksan Mo by Willie Revillame')


def traverseLinkedList():
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def insertNodeAtTheBeginning(data):
    global head
    newNode = Node(data)

    newNode.next = head
    head = newNode



insertNodeAtTheBeginning('Multo by Cuo of Joe')
insertNodeAtTheBeginning('Naiilang by Lee John')
insertNodeAtTheBeginning('Saksi ang langit by December Avenue')



def insertNodeAtTheEnd(data):
    global head
    newNode = Node(data)

    if head is None:
        head = newNode
    else:
        current = head
        while current.next:
            current = current.next
        current.next = newNode



insertNodeAtTheEnd('Lifetime by Ben&Ben')
insertNodeAtTheEnd('Yesterday Dreams by Donna Cruz')



def insertNodeAfterGivenNode(data, node):
    global head
    newNode = Node(data)

    current = head

    
    while current and current.data != node:
        current = current.next

    if current is None:
        print(f'The node "{node}" does not exist')
        return

    newNode.next = current.next
    current.next = newNode



insertNodeAfterGivenNode('Anything', 'Lifetime by Ben&Ben')
insertNodeAfterGivenNode('Who Knows', 'Saksi ang langit by December Avenue')



traverseLinkedList()