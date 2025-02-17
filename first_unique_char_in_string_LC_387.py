class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = {}

        for i in s:
            if i in a:
                a[i] = a[i] + 1
            else:
                a[i] = 1

        for index, i in enumerate(s):
            if a[i] == 1:
                return index

        return -1




