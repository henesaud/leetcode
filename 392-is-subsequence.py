class Solution(object):
    def isSubsequence(self, s, t):
        sp, tp = 0,0

        if len(s) == 0:
            return True

        while tp<len(t):
            if t[tp] == s[sp]:
                sp+=1

            if sp == len(s):
                return True

            tp+=1

        return False
