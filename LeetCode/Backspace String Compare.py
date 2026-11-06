class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
                def process(text):
                    stack = []

                    for ch in text:
                        if ch == '#':
                            if stack:
                                stack.pop()
                        else:
                            stack.append(ch)

                    return ''.join(stack)

                return process(s) == process(t)
