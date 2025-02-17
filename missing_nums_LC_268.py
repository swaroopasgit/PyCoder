class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums1 = set(nums)
        a = None
        n = len(nums1)

        for i in range(0, n + 1):
            if i not in nums1:
                a = i

        print(a)
        return a


