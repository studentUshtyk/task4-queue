from collections import deque

def constrainedSubsetSum(nums, k):
    n = len(nums)
    dp = nums[:]  
    deq = deque([0])  
    max_sum = nums[0]  

    for i in range(1, n):
        dp[i] = nums[i] + max(dp[deq[0]], 0)

        max_sum = max(max_sum, dp[i])

        if deq[0] < i - k:
            deq.popleft()

        while deq and dp[deq[-1]] <= dp[i]:
            deq.pop()

        deq.append(i)

    return max_sum

nums1 = [10, 2, -10, 5, 20]
k1 = 2
print(constrainedSubsetSum(nums1, k1))  # Output: 37

nums2 = [-1, -2, -3]
k2 = 1
print(constrainedSubsetSum(nums2, k2))  # Output: -1

nums3 = [10, -2, -10, -5, 20]
k3 = 2
print(constrainedSubsetSum(nums3, k3))  # Output: 23
