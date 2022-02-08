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

    def insert(self):
        pass

    def delete(self):
        pass

    def find(self):
        pass


tree = BinarySearchTreeTest(5)
print(tree.head.value)
# test node, works
# treeNode = TreeNode(1)
# treeNodeTwo = TreeNode(2)
# treeNodeThree = TreeNode(3)
# treeNode.leftChild = treeNodeTwo
# treeNode.rightChild = treeNodeThree
# print(treeNode.value)
# print(treeNode.leftChild.value)
# print(treeNode.rightChild.value)
