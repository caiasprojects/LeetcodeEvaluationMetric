

class Solution(object):
    def findLUSlength(self, a, b):
        longest = -1
        for i in range(len(a)):
            for j in range(i, len(a)):
                subsequence = a[i:j+1]
                if subsequence not in b:
                    longest = max(longest, len(subsequence))
        
        for i in range(len(b)):
            for j in range(i, len(b)):
                subsequence = b[i:j+1]
                if subsequence not in a:
                    longest = max(longest, len(subsequence))
        
        return longest if longest > 0 else -1