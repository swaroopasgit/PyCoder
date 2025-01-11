class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        len_of_last_word = len(word[-1])

        return len_of_last_word

