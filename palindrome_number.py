class Solution:
    def isPalindrome(self, x: int) -> bool:
        revs = []
        f = x
        if x < 0:
            return False
        while (x):
            a = x % 10
            revs.append(a)
            x = x // 10

        sums = 0
        for i in revs:
            sums = (sums * 10) + i

        if f != sums:
            return False

        return True

        print(x)
        print(sums)

