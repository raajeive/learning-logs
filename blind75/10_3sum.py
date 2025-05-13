class Solution:
    def threeSum(self, nums):
        result = set()

        for idx in range(len(nums)):
            target = 0 - nums[idx]

            data_dict = {}

            for idx2 in range(idx + 1, len(nums)):
                if nums[idx2] in data_dict:
                    triplet = (nums[idx], nums[idx2], nums[data_dict[nums[idx2]]])
                    result.add(tuple(sorted(triplet)))
                data_dict[target - nums[idx2]] = idx2
        return [list(item) for item in result]


class Solution2:
    def threeSum(self, nums):
        nums.sort()
        len_nums = len(nums)
        result = []

        for idx in range(len_nums - 2):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            
            left = idx + 1
            right = len_nums - 1

            while right > left:
                temp = nums[idx] + nums[left] + nums[right]

                if temp == 0:
                    result.append([nums[idx], nums[left], nums[right]])
                    # Skip duplicates for the second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif temp > 0:
                    right -= 1
                else:
                    left += 1
        
        return result