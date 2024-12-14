class Solution(object):
    def twoSum(self, numbers, target):
        l, r =  0 , len(numbers)-1

        while l<r:
            cur_sum = numbers[l]+numbers[r]

            if cur_sum < target:
                l+=1
            elif cur_sum > target:
                r-=1
            else:
                return [l+1,r+1]

        return []
