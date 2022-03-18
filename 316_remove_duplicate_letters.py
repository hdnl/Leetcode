# Given a string s, remove duplicate letters
# so that every letter appears once and only once.
# You must make sure your result is the smallest
# in lexicographical order among all possible results.

class Solution:

    @staticmethod
    def remove_duplicate_letters(s: str) -> str:
        char_rindex = {c: i for i, c in enumerate(s)}
        solution = []

        for i, character in enumerate(s):
            if character in solution:
                continue
            while solution and solution[-1] > character and char_rindex[solution[-1]] > i:
                solution = solution[:-1]
            solution.append(character)

        return "".join(solution)


if __name__ == '__main__':
    assert Solution.remove_duplicate_letters("bcabc") == "abc"
    assert Solution.remove_duplicate_letters("cbacdcbc") == "acdb"
