

import collections

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.isWord = False
        self.word = ""

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        for c in word:
            cVal = ord(c) - ord("a")
            if not p.children[cVal]:
                p.children[cVal] = TrieNode()
            p = p.children[cVal]

        p.isWord = True
        p.word = word

    def helper(self, word):
        p = self.root
        for c in word:
            cVal = ord(c) - ord("a")
            if not p.children[cVal]:
                return None
            p = p.children[cVal]
        return p

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.helper(word)
        if p and p.isWord:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.helper(prefix)
        if p:
            return True
        return False