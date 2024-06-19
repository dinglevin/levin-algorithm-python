from typing import List


class Solution:
    def two_sum_v1(nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
        return [0, 0]

    def two_sum_v2(nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            comp_index = map.get(complement)
            if comp_index is not None:
                return [comp_index, i]
            map[nums[i]] = i

        return [0, 0]

    def two_sum_v3(nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        left = 0
        right = len(nums) - 1

        while left < right:
            sum = sorted_nums[left] + sorted_nums[right]
            if sum == target:
                return [nums.index(sorted_nums[left]),
                        next(i for i in range(len(nums) - 1, -1, -1)
                             if nums[i] == sorted_nums[right])
                        ]
            elif sum < target:
                left += 1
            else:
                right -= 1

        return [0, 0]
