# There is a broken calculator that has the integer startValue
# on its display initially. In one operation, you can:
#
#     multiply the number on display by 2, or
#     subtract 1 from the number on display.
#
# Given two integers startValue and target,
# return the minimum number of operations needed to display target on the calculator.

class Solution:
    @staticmethod
    def broken_calc(start_value: int, target: int) -> int:
        ans = 0
        while target > start_value:
            target = target + 1 if target % 2 else target // 2
            ans += 1

        return ans + start_value - target


if __name__ == '__main__':
    assert Solution.broken_calc(start_value=2, target=3) == 2  # 2 * 2 = 4; 4 - 3 = 1
    assert Solution.broken_calc(start_value=5, target=8) == 2  # 5 - 1 = 4; 4 * 2 = 8
    assert Solution.broken_calc(start_value=3, target=10) == 3  # 3 * 2 = 6; 6 - 1 = 5; 5 - 1 = 4; 4 * 2 = 8
    assert Solution.broken_calc(start_value=1024, target=1) == 1023
    assert Solution.broken_calc(start_value=1, target=1000000000) == 39
