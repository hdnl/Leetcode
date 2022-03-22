# The numeric value of a lowercase character is defined as
# its position (1-indexed) in the alphabet,
# so the numeric value of a is 1,
# the numeric value of b is 2,
# the numeric value of c is 3, and so on.
#
# The numeric value of a string consisting of lowercase characters
# is defined as the sum of its characters' numeric values.
# For example, the numeric value of the string "abe"
# is equal to 1 + 2 + 5 = 8.
#
# You are given two integers n and k.
# Return the lexicographically smallest string with
# length equal to n and numeric value equal to k.
#
# Note that a string x is lexicographically smaller than string y
# if x comes before y in dictionary order, that is,
# either x is a prefix of y, or if i is the first position
# such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.


class Solution:
    @staticmethod
    def get_smallest_string(n: int, k: int) -> str:
        k -= n
        ans = ['a'] * n
        i = n - 1
        while k > 0:
            ans[i] = chr(ord(ans[i]) + min(k, 25))
            k -= min(k, 25)
            i -= 1
        return ''.join(ans)


if __name__ == '__main__':
    assert Solution.get_smallest_string(n=3, k=27) == "aay"
    assert Solution.get_smallest_string(n=5, k=73) == "aaszz"
