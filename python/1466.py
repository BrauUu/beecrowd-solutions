class Node:
    def __init__(self, content):
        self.content = content
        self.leftNode = None
        self.rightNode = None  

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, content: int):
        self.root = self.__recursiveInsert(self.root, content)
        
    def __recursiveInsert(self, node: Node, content: int):
        if node == None:
            return Node(content)
        elif content > node.content:
            node.rightNode = self.__recursiveInsert(node.rightNode, content)
        elif content < node.content:
            node.leftNode = self.__recursiveInsert(node.leftNode, content)
        return node

    def breadthFirstSearch(self):
        queue = [self.root]
        levelList = []
        while len(queue) != 0:
            node = queue.pop(0)
            levelList.append(node.content)
            leftNode = node.leftNode
            rightNode = node.rightNode
            if leftNode != None:
                queue.append(leftNode)
            if rightNode != None:
                queue.append(rightNode)
        return levelList

c = int(input())
for i in range(1, c+1):
    n = int(input())
    values = list(map(int, input().split()))
    bst = BinarySearchTree()
    for value in values:
        bst.insert(value)
    levelList = bst.breadthFirstSearch()
    print(f"Case {i}:")
    print(*levelList, sep=" ")
    print()