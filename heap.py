# implement arr based heap from algo book
import numpy as np
# arr = np.array([])
# print(type(arr))


class HeapTest:
    # heap using internal array rather than tree / nodes
    def __init__(self) -> None:
        self.data = []

    def print_heap(self):
        print(self.data)

    def root_node(self):
        return self.data[0]

    def last_node(self):
        return self.data[-1]

    # returns the correct index of the left child from a given index
    def left_child_index(self, index):
        return int(np.floor((index * 2) + 1))

    # returns the correct index of the right child from a given index
    def left_child_index(self, index):
        return int(np.floor((index * 2) + 2))

    # returns the parent node of a given index
    def parent_index(self, index):
        return int(np.floor((index-1) / 2))

    # adds value at the end(last node) and traverses it up the 'tree' to the correct place
    def insert(self, value):
        # add to list
        self.data.append(value)
        # keep track of index of new node
        new_node_index = len(self.data) - 1

        # trickle up

        # if the new node is not in the root position
        # and its greater than its parent node:
        while (new_node_index > 0 and
               self.data[new_node_index] > self.data[int(self.parent_index(new_node_index))]):
            parent = self.data[int(self.parent_index(new_node_index))]
            # swap the new node with its parent node:
            print(parent)
            print("parent", self.parent_index(new_node_index))
            temp = self.data[parent]
            self.data[parent] = self.data[new_node_index]
            self.data[new_node_index] = temp

            # update the index of the new node
            new_node_index = self.parent_index(new_node_index)
            # print(new_node_index)


heap = HeapTest()
heap.insert(1)
heap.insert(4)
heap.insert(6)
heap.insert(9)
heap.print_heap()
