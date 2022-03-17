from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def manhattan_distance(p1: List[int], p2: List[int]):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    @staticmethod
    def assign_bikes(workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        res = [-1] * len(workers)
        distances = defaultdict(list)
        for w_idx, worker in enumerate(workers):
            for b_idx, bike in enumerate(bikes):
                distances[Solution.manhattan_distance(worker, bike)].append([w_idx, b_idx])

        for k in sorted(distances.keys()):
            for pair in distances[k]:
                if res[pair[0]] == -1 and pair[1] not in res:
                    res[pair[0]] = pair[1]
            if -1 not in res:
                break

        return res


if __name__ == '__main__':
    assert Solution.assign_bikes(workers=[[0, 0], [2, 1]], bikes=[[1, 2], [3, 3]]) == [1, 0]
    assert Solution.assign_bikes(workers=[[0, 0], [1, 1], [2, 0]], bikes=[[1, 0], [2, 2], [2, 1]]) == [0, 2, 1]
    workers = [[240, 446], [745, 948], [345, 136], [341, 68], [990, 165], [165, 580], [133, 454], [113, 527]]
    bikes = [[696, 140], [95, 393], [935, 185], [767, 205], [387, 767], [214, 960], [804, 710], [956, 307]]
    assert Solution.assign_bikes(workers=workers, bikes=bikes) == [7,6,0,3,2,4,1,5]