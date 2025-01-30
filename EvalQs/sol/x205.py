

class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        s_map = {}  # Store mappings from s to t
        t_map = {}  # Store mappings from t to s

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s in s_map and s_map[char_s] != char_t:
                return False  # Mismatch in mappings
            if char_t in t_map and t_map[char_t] != char_s:
                return False  # Mismatch in mappings

            s_map[char_s] = char_t
            t_map[char_t] = char_s

        return True