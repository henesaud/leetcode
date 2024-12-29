class Solution(object):
    def longestConsecutive(self, nums):
        longest = 0
        num_set = set(nums)
        for n in num_set:
            if not n-1 in nums:
                length = 0
                while n+length in nums:
                    length+=1

                longest = max(longest, length)

        return longest
