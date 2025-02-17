import math


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""
        a = math.inf
        b = None
        for word in strs:
            if len(word) < a:
                b = word
                a = len(word)

        c = ""
        for word in strs:
            for index, i in enumerate(b):
                if b[index] == word[index]:
                    c = c + i
                else:
                    break
            b = c
            c = ""
        return b

