class Solution(object):
    def groupAnagrams(self, strs):
        res  = {}

        for s in strs:
            # just lower case letters are allowed. So, there are 26 possibilities
            count = [0]*26

            for c in s:
                count[ord(c)-ord("a")] +=1

            count_tuple = tuple(count)
            if res.get(tuple(count)):
                res[count_tuple].append(s)
            else:
                res[count_tuple] =[s]

        return res.values()
