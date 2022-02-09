class TreeNode:
    def __init__(self, value=None, left=None, right=None) -> None:
        self.value = value
        self.leftChild = left
        self.rightChild = right

    # def getRightChild(self):
    #     return self.rightChild

    # def getLeftChild(self):
    #     return self.leftChild

    # def setRightChild(self, value):
    #     self.RightChild = TreeNode(value)

    # def setLeftChild(self, value):
    #     self.leftChild = TreeNode(value)


class BinarySearchTreeTest:
    def __init__(self, value) -> None:
        self.head = TreeNode(value)

    def insert(self, num, currentNode):
        if num < currentNode.value:
            # insert as left child
            if currentNode.leftChild == None:
                currentNode.leftChild = TreeNode(num)
            else:
                self.insert(num, currentNode.leftChild)
        elif num > currentNode.value:
            if currentNode.rightChild == None:
                currentNode.rightChild = TreeNode(num)
            else:
                self.insert(num, currentNode.rightChild)

    def lift(self, node, nodeToDelete):
        if node.leftChild:
            node.leftChild = self.lift(node.leftChild, nodeToDelete)
            return node
        else:
            nodeToDelete.value = node.value
            return node.rightChild

    def delete(self, num, currentNode):
        # base case
        if currentNode is None:
            return None

        elif num < currentNode.value:
            currentNode.leftChild = self.delete(num, currentNode.leftChild)
            return currentNode

        elif num > currentNode.value:
            currentNode.rightChild = self.delete(num, currentNode.rightChild)
            return currentNode

        elif num == currentNode.value:
            if currentNode.leftChild is None:
                return currentNode.rightChild

            elif currentNode.rightChild is None:
                return currentNode.leftChild

            else:
                currentNode.rightChild = self.lift(
                    currentNode.rightChild, currentNode)
                return currentNode

    def find(self, num, currentNode):
        # number found/ base case
        if currentNode is None or currentNode.value == num:
            return currentNode.value
        # search above current node
        elif num < currentNode.value:
            return self.find(num, currentNode.leftChild)
        # search below current node
        else:
            return self.find(num, currentNode.rightChild)

    def print_tree(self, node, arr=[]):
        if node is None:
            return

        self.print_tree(node.leftChild, arr)
        print(node.value)
        self.print_tree(node.rightChild, arr)


tree = BinarySearchTreeTest(5)
tree.insert(6, tree.head)
tree.insert(2, tree.head)
tree.insert(4, tree.head)
tree.insert(9, tree.head)
tree.print_tree(tree.head)
tree.delete(4, tree.head)
tree.delete(2, tree.head)
tree.delete(9, tree.head)
tree.print_tree(tree.head)
# test node, works
# treeNode = TreeNode(1)
# treeNodeTwo = TreeNode(2)
# treeNodeThree = TreeNode(3)
# treeNode.leftChild = treeNodeTwo
# treeNode.rightChild = treeNodeThree
# print(treeNode.value)
# print(treeNode.leftChild.value)
# print(treeNode.rightChild.value)
