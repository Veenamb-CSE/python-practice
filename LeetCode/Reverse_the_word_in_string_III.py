class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_text = "".join(reversed(s))
        reversed_text=reversed_text.split()
        reversed_list = list(reversed(reversed_text))
        reversed_text=" " .join(reversed_list)
        return reversed_text
