class Solution:
    def canJump(self, nums):
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1

        return True





solution = Solution()
print(solution.canJump([2,0]))