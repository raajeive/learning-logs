class Solution:
    def removeDuplicates(self, nums):
        size = len(nums)
        if size < 2:
            return size
        pos = None
        index = 0
        while index < size:
            if pos is None or nums[index] != nums[pos]:
                pos = pos + 1 if pos is not None else 0
                nums[pos] = nums[index]
                if index + 1 < size and nums[index] == nums[index + 1]:
                    pos += 1
                    nums[pos] = nums[index + 1]
                    index += 1
            index += 1
        return pos + 1
