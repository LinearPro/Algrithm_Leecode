class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        i = len(nums) - 1
        rst = [float('inf')] * len(nums)
        # 数组表示 [0] * n
        while left <= right:
            if nums[left] ** 2 >= nums[right] ** 2:
                rst[i] = nums[left] ** 2
                left += 1
            else:
                rst[i] = nums[right] ** 2
                right -= 1
            i -= 1
        return rst
