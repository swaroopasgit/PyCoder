class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        for index, i in enumerate(haystack):
            req = haystack[index:index + len(needle)]
            if req == needle:
                return index

        return -1
