class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0 

        while r < len(nums):
            count = 0 
            while r+1 < len(nums) and nums[r] == nums[r+1]:
                count+= 1
                r+=1
            
            repetitions = min(2, count)
            for _ in range(repetitions):
                nums[l] = nums[r]
                l+=1
            r+=1

        return l
