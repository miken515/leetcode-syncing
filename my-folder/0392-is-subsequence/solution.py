class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == '': return True

        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                if j == len(s) - 1:
                    return True
                j += 1

        return False
