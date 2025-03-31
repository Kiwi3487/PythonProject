class TernaryTrie:
    def __init__(self, char):
        self.char = char
        self.left = self.middle = self.right = None
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = None
        self.word_list = []

    def add(self, word):
        self.root = self.checkadd(self.root, word, 0)
        if word not in self.word_list:
            self.word_list.append(word)

    def checkadd(self, node, word, index):
        if node is None:
            node = TernaryTrie(word[index])
        if word[index] < node.char:
            node.left = self.checkadd(node.left, word, index)
        elif word[index] > node.char:
            node.right = self.checkadd(node.right, word, index)
        else:
            if index + 1 == len(word):
                node.is_end_of_word = True
            else:
                node.middle = self.checkadd(node.middle, word, index + 1)
        return node

    def search(self, prefix):
        node = self.checksearch(self.root, prefix, 0)
        if node:
            return self.findwords(node, prefix[:-1])
        return []

    def checksearch(self, node, prefix, index):
        if node is None:
            return None
        if prefix[index] < node.char:
            return self.checksearch(node.left, prefix, index)
        elif prefix[index] > node.char:
            return self.checksearch(node.right, prefix, index)
        else:
            if index + 1 == len(prefix):
                return node
            return self.checksearch(node.middle, prefix, index + 1)

    def findwords(self, node, prefix):
        words = []
        if node is None:
            return words
        if node.is_end_of_word:
            words.append(prefix + node.char)
        words.extend(self.findwords(node.left, prefix))
        if node.middle:
            words.extend(self.findwords(node.middle, prefix + node.char))
        words.extend(self.findwords(node.right, prefix))
        return words

    def displaylist(self):
        return self.word_list

trie = Trie()
while True:
    action = input("Enter 'a' to insert a word, 's' to search for suggestions, 'l' to view current word bank or 'e' to quit: ").strip().lower()
    if action == 'a':
        word = input("Enter a word to add: ").strip()
        trie.add(word)
    elif action == 's':
        prefix = input("Enter prefix to search: ").strip()
        print("Suggestions:", trie.search(prefix))
    elif action == 'l':
        print("List words added: ", trie.displaylist())
    elif action == 'e':
        break
    else:
        print("Invalid command. Try again.")
