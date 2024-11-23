from typing import List


class Solution:
	def jump(self, nums: List[int]) -> int:
		max_i = 0
		current_i = 0
		jumps = 0
		size = len(nums) - 1


		for i in range(size):
			#determines the max index possible to jump
			max_i = max(max_i, i + nums[i])

			#checks if can jump to the last position
			if max_i >= size:
				jumps+= 1
				break

			#checks if all jumps possibilities were checked
			if current_i == i:
				jumps+= 1
				current_i = max_i

		return jumps
