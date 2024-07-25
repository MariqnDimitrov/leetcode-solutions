class Solution(object):
    def removeElement(self, nums, val):
        val_count = nums.count(val)
        while val_count > 0:
            nums.remove(val)
            val_count -= 1
        return nums

solution = Solution()
print(solution.removeElement([3,2,2,3], 3))