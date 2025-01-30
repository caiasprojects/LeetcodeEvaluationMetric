

from collections import Counter

class Solution(object):
    def canPermutePalindrome(self, s):
        char_counts = Counter(s)  # Use Counter for efficient counting
        odd_count = sum(1 for count in char_counts.values() if count % 2 == 1)
        return odd_count <= 1  # Check if there's at most one odd count