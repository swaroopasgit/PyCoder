class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        for index, value in enumerate(nums):
            req_num = target - value
            if req_num in a:
                return [a[req_num], index]
            else:
                a[value] = index




