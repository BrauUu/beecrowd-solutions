class Node:
    def __init__(self, content):
        self.content = content
        self.leftNode = None
        self.rightNode = None

class BinarySearchTree:
    
    def __init__(self):
        self.root = None

    def insert(self, content):
        self.root = self.__recursiveInsert(self.root, content)

    def __recursiveInsert(self, node: Node, content):
        if node == None:
            return Node(content)
        elif content > node.content:
            node.rightNode = self.__recursiveInsert(node.rightNode, content)
        elif content < node.content:
            node.leftNode = self.__recursiveInsert(node.leftNode, content)
        return node

    def preOrder(self):
        res = []
        response = ""
        self.__recursivePreOrder(self.root, res)
        for item in res:
            response += str(item) + " "
        return response.strip()

    def __recursivePreOrder(self, node: Node, res: list):
        if node != None:
            res.append(node.content)
            self.__recursivePreOrder(node.leftNode, res)
            self.__recursivePreOrder(node.rightNode, res)

    def inOrder(self):
        res = []
        response = ""
        self.__recursiveInOrder(self.root, res)
        for item in res:
            response += str(item) + " "
        return response.strip()

    def __recursiveInOrder(self, node: Node, res: list):
        if node != None:
            self.__recursiveInOrder(node.leftNode, res)
            res.append(node.content)
            self.__recursiveInOrder(node.rightNode, res)

    def postOrder(self):
        res = []
        response = ""
        self.__recursivePostOrder(self.root, res)
        for item in res:
            response += str(item) + " "
        return response.strip()
    
    def __recursivePostOrder(self, node: Node, res: list):
        if node != None:
            self.__recursivePostOrder(node.leftNode, res)
            self.__recursivePostOrder(node.rightNode, res)
            res.append(node.content)


n = int(input())

for i in range(n):
    
    bst = BinarySearchTree()
    
    arrSize = int(input())
    numArr = list(map(int, input().split()))

    for item in numArr:
        bst.insert(item)

    print(f"Case {i+1}:")
    print(f"Pre.: {bst.preOrder()}")
    print(f"In..: {bst.inOrder()}")
    print(f"Post: {bst.postOrder()}")
    print('')
    
