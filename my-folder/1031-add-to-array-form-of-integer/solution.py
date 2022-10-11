class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = ""
        ansl = []
        
        for i in num:
            ans += str(i)
            
        ans = int(ans) + k
        
        for i in str(ans):
            ansl.append(i)
            
        return ansl
