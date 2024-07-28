class Solution(object):
    def jump(self, nums):
        near = far = jumps = 0
        while far < len(nums) - 1:
            farthest = 0
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])
            near = far + 1
            far = farthest
            jumps += 1
        return jumps





solution = Solution()
print(solution.jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))
