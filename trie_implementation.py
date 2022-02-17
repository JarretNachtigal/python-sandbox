# these are notes from algo book
class Trie_Node:
    def __init__(self) -> None:
        self.children = {}


class Trie:
    def __init__(self) -> None:
        self.root = Trie_Node()

    def printWords(self, node=None, word="", words=[]):
        # This method accepts three arguments. The first is the
        # node whose descendants we're collecting words from.
        # The second argument, word, begins as an empty string,
        # and we add characters to it as we move through the trie.
        # The third argument, words, begins as an empty array,
        # and by the end of the function will contain all the words
        # from the trie.
        # The current node is the node passed in as the first parameter,
        # or the root node if none is provided:
        currentNode = node or self.root

        # we iterate through all the current nodes children
        for key, childNode in currentNode.children.items():
            # if the current key is *, it means we hit
            # the end of a complete word, so we can add it to out words array:
            if key == "*":
                words.append(word)
            else:
                # we are still in the middle of a word
                # recursively call this function on the child node
                # child node, concatenate word, memoize words
                self.printWords(childNode, word + key, words)
        return words

    def insert(self, word):
        currentNode = self.root

        for char in word:
            # if the current node has child key with the current character:
            if currentNode.children.get(char):
                # follow the child node:
                currentNode = currentNode.children[char]
            else:
                # if the current character isnt found among the current nodes children,
                # we add the character as ta new child node:
                newNode = Trie_Node()
                currentNode.children[char] = newNode

                # follow this to the new node
                currentNode = newNode
        # after inserting the whole word into the trie
        # we add a * to mark the end
        currentNode.children["*"] = None

    def search(self, word):
        currentNode = self.root

        for char in word:
            # if current node has a key with current character
            if currentNode.children.get(char):
                # follow the child node
                currentNode = currentNode.children[char]
            else:
                # word not in trie
                return None
        return currentNode


trie = Trie()
trie.insert("gamer")
trie.insert("goop")
trie.insert("cringe")
print(trie.printWords())
