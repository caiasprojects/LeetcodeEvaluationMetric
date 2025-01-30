

import collections

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_count = collections.Counter(s)
        t_count = collections.Counter(t)

        return s_count == t_count