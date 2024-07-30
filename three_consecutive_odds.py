class Solution(object):
    def threeConsecutiveOdds(self, arr):
        for i in range(0, len(arr)):
            filtered_arr = list(filter(lambda x: x % 2 != 0, arr[i:i+3]))
            if len(filtered_arr) == 3:
                return True
        return False


solution = Solution()
print(solution.threeConsecutiveOdds([2,6,4,1]))