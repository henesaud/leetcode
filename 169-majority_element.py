class Solution(object):
    def majorityElement(self, nums):
        count, result = 0 , nums[0]

        for n in nums:
            if count == 0:
                result = n

            count += (1 if n==result else -1)

        return result
