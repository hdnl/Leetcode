# https://leetcode.com/problems/validate-stack-sequences/
# Given two integer arrays pushed and popped each with distinct values
# Return true if this could have been the result of a sequence of
# push and pop operations on an initially empty stack
# or false otherwise.

from typing import List


class Solution:
    @staticmethod
    def validate_stack_sequences(pushed: List[int], popped: List[int]) -> bool:
        left_pointer = 0

        while popped:
            idx_to_pop = pushed.index(popped.pop(0))
            if idx_to_pop >= left_pointer:
                pushed.pop(idx_to_pop)
                left_pointer = idx_to_pop - 1
            else:
                return False

        return True


if __name__ == '__main__':
    assert Solution.validate_stack_sequences(pushed=[], popped=[])
    assert Solution.validate_stack_sequences(pushed=[1, 2], popped=[2, 1])
    assert Solution.validate_stack_sequences(pushed=[1, 2, 3], popped=[3, 2, 1])
    assert not Solution.validate_stack_sequences(pushed=[1, 2, 3], popped=[3, 1, 2])
    assert Solution.validate_stack_sequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1])
    assert not Solution.validate_stack_sequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2])
