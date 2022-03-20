# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino.
# (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
#
# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
#
# Return the minimum number of rotations so that all the values in tops are the same,
# or all the values in bottoms are the same.
#
# If it cannot be done, return -1.

from typing import List


class Solution:
    @staticmethod
    def min_domino_rotations(tops: List[int], bottoms: List[int]) -> int:
        def needed_rotations(x):
            needed_top_rotations = needed_bottom_rotations = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                elif tops[i] != x:
                    needed_top_rotations += 1
                elif bottoms[i] != x:
                    needed_bottom_rotations += 1
            return min(needed_top_rotations, needed_bottom_rotations)

        rotations = needed_rotations(tops[0])
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations
        return needed_rotations(bottoms[0])


if __name__ == '__main__':
    assert Solution.min_domino_rotations(tops=[2, 1, 2, 4, 2, 2], bottoms=[5, 2, 6, 2, 3, 2]) == 2
    assert Solution.min_domino_rotations(tops=[3, 5, 1, 2, 3], bottoms=[3, 6, 3, 3, 4]) == -1
