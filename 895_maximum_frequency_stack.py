# Design a stack-like data structure to push elements
# to the stack and pop the most frequent element from the stack.
#
# Implement the FreqStack class:
#
#     FreqStack() constructs an empty frequency stack.
#     void push(int val) pushes an integer val onto the top of the stack.
#     int pop() removes and returns the most frequent element in the stack.
#         If there is a tie for the most frequent element,
#         the element closest to the stack's top is removed and returned.
from collections import Counter, defaultdict


class FreqStack:
    def __init__(self):
        self.element_freq = Counter()
        self.map_by_freq = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.element_freq[val] += 1
        self.max_freq = max(self.max_freq, self.element_freq[val])
        self.map_by_freq[self.element_freq[val]].append(val)

    def pop(self) -> int:
        x = self.map_by_freq[self.max_freq].pop()
        if not self.map_by_freq[self.max_freq]:
            self.max_freq -= 1
        self.element_freq[x] -= 1
        return x


if __name__ == '__main__':
    obj = FreqStack()
    obj.push(5)
    obj.push(7)
    obj.push(5)
    obj.push(7)
    obj.push(4)
    obj.push(5)
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
