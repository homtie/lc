class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        n = len(nums)

        # Step 1: Find pivot
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: Find element just larger than pivot
        if i >= 0:

            j = n - 1

            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse everything after pivot
        left = i + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1