class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum = 0
        max_1 = []
        for i in nums:
            if i == 1:
                sum = sum + 1
            else:
                max_1.append(sum)
                sum = 0

        max_1.append(sum)

        req = max(max_1)

        return req
