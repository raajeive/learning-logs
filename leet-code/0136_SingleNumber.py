from functools import reduce
class Solution:
    def singleNumber(self, nums):
        # res = 0
        # for num in nums:
        #     res = res ^ num
        # return res
        return reduce(lambda a, b : a ^ b, nums, 0)
