```python
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        list = sentence.split()

        for i in range(0, len(list)):
            if list[i].startswith(searchWord):
                return i + 1

        return -1
```
