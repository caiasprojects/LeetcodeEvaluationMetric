

from typing import List

class Solution:
    def toLowerCase(self, str):
        return ''.join(chr(ord(c) + 32) if ord(c) >= 65 and ord(c) <= 90 else c for c in str)