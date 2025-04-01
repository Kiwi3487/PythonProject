class StandardTrie:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = StandardTrie()
        self.word_list = []

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = StandardTrie()
            node = node.children[char]
        if not node.is_end_of_word:
            self.word_list.append(word)
        node.is_end_of_word = True

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self.findwords(node, prefix)

    def findwords(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, next_node in node.children.items():
            words.extend(self.findwords(next_node, prefix + char))
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
        print("List words added:", trie.displaylist())
    elif action == 'e':
        break
    else:
        print("Input invalid")