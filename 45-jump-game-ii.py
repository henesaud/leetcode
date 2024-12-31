from typing import List


class Solution:
	def jump(self, nums: List[int]) -> int:
		max_i = 0
		current_max = 0
		jumps = 0
		size = len(nums) - 1

		#perceive: it goes to the last position -1, not the final one
		for i in range(size):
			#determines the max index possible to jump
			max_i = max(max_i, i + nums[i])

			#checks if can jump to the last position
			if max_i >= size:
				jumps+= 1
				break

			#checks if all jumps possibilities were checked
			if current_max == i:
				jumps+= 1
				current_max = max_i

		return jumps




class Solution2:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        result = 0

		#perceive: it goes to the last position -1, not the final one
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            
            l = r+1
            r = farthest
            result +=1

        return result
