class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            if i in a:
                a[i] = a[i] + 1
            else:
                a[i] = 1

        for key, value in a.items():
            if value == 1:
                return key
