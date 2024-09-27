class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()

        reverseWords = reversed(words)

        reverseSentence = ' '.join(reverseWords)

        return reverseSentence
