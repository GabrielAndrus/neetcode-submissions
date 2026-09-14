class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            midpoint = (low + high) // 2

            if nums[midpoint] == target:
                return midpoint

            # target on right, update the lower boundary
            elif nums[midpoint] < target:
                low = midpoint + 1

            # target on left, update higher boundary
            else:
                high = midpoint - 1

        return -1