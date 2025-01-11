class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = {}
        n = len(nums)
        for i in nums:
            if i in a:
                a[i] = a[i] + 1
            else:
                a[i] = 1

        for key, value in a.items():
            if value > n / 2:
                return key