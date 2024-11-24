from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [1]*size

        prefix = 1
        for i in range(size):
            res[i] *= prefix
            prefix*=nums[i]

        posfix = 1
        for i in range(size-1, -1,-1):
            res[i]*= posfix
            posfix*= nums[i]

        return res
