# You are given a string s.
# We want to partition the string into as many parts as possible
# so that each letter appears in at most one part.
#
# Note that the partition is done so that
# after concatenating all the parts in order,
# the resultant string should be s.
#
# Return a list of integers representing the size of these parts.

from typing import List


class Solution:
    @staticmethod
    def partition_labels(s: str) -> List[int]:
        # find last occurrence of each character
        char_rindex = {c: i for i, c in enumerate(s)}
        start = end = 0
        solution = []

        for i, character in enumerate(s):
            end = max(end, char_rindex[character])
            if i == end:
                solution.append(i - start + 1)
                start = i + 1

        return solution


if __name__ == '__main__':
    assert Solution.partition_labels(s="ababcbacadefegdehijhklij") == [9, 7, 8]
    assert Solution.partition_labels(s="eccbbbbdec") == [10]
