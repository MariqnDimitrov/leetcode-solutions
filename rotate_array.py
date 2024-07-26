from collections import deque
class Solution(object):
    def rotate(self, nums, k):
        result_nums = deque(nums)
        for i in range(k):
            rotating_number = result_nums.pop()
            result_nums.appendleft(rotating_number)
        nums[::] = list(result_nums)[::]
        return nums

solution = Solution()
print(solution.rotate([1,2,3,4,5,6,7], 3))
