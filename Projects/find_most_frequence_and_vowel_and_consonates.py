class Solution:
    def maxFreqSum(self, s: str) -> int:

        con = []
        vow = []

        vowels = ['a', 'e', 'i', 'o', 'u']

        for i in s:
            if i in vowels:
                vow.append(i)
            else:
                con.append(i)

        val1 = []
        val2 = []

        for i in range(len(vow)):
            val1.append(vow.count(vow[i]))

        for i in range(len(con)):
            val2.append(con.count(con[i]))

        vowel_max = max(val1) if val1 else 0
        consonant_max = max(val2) if val2 else 0

        return vowel_max + consonant_max

        val1 = []
        val2 = []

        for i in range(0, len(vow)):
            val1.append(vow.count(vow[i]))

        for i in range(0, len(con)):
            val2.append(con.count(con[i]))

        vowel_max = max(val1) if val1 else 0
        consonant_max = max(val2) if val2 else 0

        return vowel_max + consonant_max
