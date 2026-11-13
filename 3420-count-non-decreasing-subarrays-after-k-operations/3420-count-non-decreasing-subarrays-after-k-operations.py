
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dq = deque()
        j = n - 1
        cost = 0
        ans = 0

        for i in range(n - 1, -1, -1):

            # Merge smaller elements into the current value
            while dq and nums[dq[-1]] < nums[i]:
                l = dq.pop()
                r = dq[-1] if dq else j + 1

                cost += (r - l) * (nums[i] - nums[l])

            dq.append(i)

            # Shrink window until cost <= k
            while cost > k:
                rightmost = dq[0]

                cost -= nums[rightmost] - nums[j]

                if rightmost == j:
                    dq.popleft()

                j -= 1

            # Count valid subarrays starting at i
            ans += j - i + 1

        return ans
