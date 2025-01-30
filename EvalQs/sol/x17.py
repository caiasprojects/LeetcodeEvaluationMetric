

import collections

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        d = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        n = len(digits)
        res = collections.deque()

        def backtrack(index, path):
            if index == n:
                res.append("".join(path))
                return

            digit = int(digits[index])
            for c in d[digit]:
                path.append(c)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return list(res)