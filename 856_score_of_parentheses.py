# Given a balanced parentheses string s, return the score of the string.
#
# The score of a balanced parentheses string is based on the following rule:
#
#     "()" has score 1.
#     AB has score A + B, where A and B are balanced parentheses strings.
#     (A) has score 2 * A, where A is a balanced parentheses string.


class Solution:
    @staticmethod
    def score_of_parentheses(s: str) -> int:
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                last_entry = stack.pop()
                if last_entry == '(':
                        stack.append(1)
                else:
                    while stack and isinstance(stack[-1], int):
                        last_entry += stack.pop()
                    if stack[-1] == '(':
                        stack.pop()
                    stack.append(last_entry * 2)

        return sum(stack)


if __name__ == '__main__':
    assert Solution.score_of_parentheses("()") == 1
    assert Solution.score_of_parentheses("(())") == 2
    assert Solution.score_of_parentheses("()()()()") == 4
    assert Solution.score_of_parentheses("((()))") == 4
    assert Solution.score_of_parentheses("()(())") == 3