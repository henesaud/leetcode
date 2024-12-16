class Solution(object):
    def minSubArrayLen(self, target, nums):
        l, total = 0,0
        res = float("inf")

        for r, element in enumerate(nums):
            total+=element

            while total >= target:
                total-=nums[l]
                res = min(res, r-l+1)
                l+=1

        return 0 if res == float("inf") else res
