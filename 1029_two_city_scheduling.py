# A company is planning to interview 2n people.
# Given the array costs where costs[i] = [aCosti, bCosti],
# the cost of flying the ith person to city a is aCosti,
# and the cost of flying the ith person to city b is bCosti.
#
# Return the minimum cost to fly every person to a city
# such that exactly n people arrive in each city.

from typing import List


class Solution:
    @staticmethod
    def two_city_sched_cost(costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        return sum([cost[0] for cost in costs[:n]] + [cost[1] for cost in costs[n:]])


if __name__ == '__main__':
    assert Solution.two_city_sched_cost(costs=[[10, 20], [30, 200], [400, 50], [30, 20]]) == 110
    assert Solution.two_city_sched_cost(costs=[[259, 770], [448, 54], [926, 667], [184, 139],
                                               [840, 118], [577, 469]]) == 1859
    assert Solution.two_city_sched_cost(costs=[[515, 563], [451, 713], [537, 709], [343, 819],
                                               [855, 779], [457, 60], [650, 359], [631, 42]]) == 3086
