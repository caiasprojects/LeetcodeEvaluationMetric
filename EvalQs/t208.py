
from sol.x208 import Trie
# Test case 1
trie = Trie()
assert trie.insert("apple") == None
assert trie.search("apple") == True
assert trie.search("app") == False
assert trie.startsWith("app") == True
assert trie.insert("app") == None
assert trie.search("app") == True

# Test case 2
assert trie.insert("orange") == None
assert trie.insert("banana") == None
assert trie.insert("grape") == None
assert trie.search("orange") == True
assert trie.search("kiwi") == False
assert trie.startsWith("ban") == True

# Test case 3
assert trie.insert("banana") == None
assert trie.search("banana") == True
assert trie.startsWith("ban") == True
assert trie.startsWith("gr") == True
assert trie.search("grape") == True

