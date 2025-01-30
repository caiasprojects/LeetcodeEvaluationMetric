

import collections

class Solution(object):
    def wordPattern(self, pattern, str):
        str = str.split()
        
        # Use a dictionary to store the mapping between pattern and string
        mapping = collections.defaultdict(lambda: [])
        
        # Iterate through the pattern and string
        for i in range(len(pattern)):
            for j in range(len(str)):
                # If the pattern element matches the string element, add the pair to the mapping
                if pattern[i] == pattern[j]:
                    mapping[pattern[i]].append(str[j])
        
        # Check if the length of the pattern and string are equal and the number of unique elements in the mapping is equal to the length of the pattern and string
        return len(pattern) == len(str) and len(set(mapping.keys())) == len(set(pattern)) == len(set(str))