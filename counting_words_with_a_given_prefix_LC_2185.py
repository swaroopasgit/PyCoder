class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        a = 0
        b = len(pref)
        for word in words:
            if word[0:b] == pref:
                a = a + 1

        return a
