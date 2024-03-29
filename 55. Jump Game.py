class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        curr = nums[0]
        for i in range(len(nums)):
            reach = max(reach,i + nums[i])
            if i == curr:
                curr = reach
        return curr >= len(nums)-1
