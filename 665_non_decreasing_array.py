# Given an array nums with n integers,
# your task is to check if it could become non-decreasing
# by modifying at most one element.
#
# We define an array is non-decreasing
# if nums[i] <= nums[i + 1] holds for every i (0-based)
# such that (0 <= i <= n - 2).

from typing import List


class Solution:
    @staticmethod
    def checkPossibility(nums: List[int]) -> bool:
        flag = False
        for idx in range(1, len(nums)):
            if nums[idx - 1] > nums[idx]:
                if flag:
                    return False
                flag = True
                if idx < 2 or nums[idx - 2] <= nums[idx]:
                    nums[idx - 1] = nums[idx]
                else:
                    nums[idx] = nums[idx - 1]
        return True


if __name__ == '__main__':
    assert not Solution.checkPossibility(nums=[2, 3, 1, 3, 1])
    assert Solution.checkPossibility(nums=[2, 3, 1, 3])
    assert Solution.checkPossibility(nums=[2, 3, 1, 3])
    assert not Solution.checkPossibility(nums=[2, 3, 1, 1])
    assert Solution.checkPossibility(nums=[4, 2, 3])
    assert Solution.checkPossibility(nums=[2, 2, 1])
    assert not Solution.checkPossibility(nums=[5, 2, 1])
    assert Solution.checkPossibility(nums=[-1,4,2,3])
