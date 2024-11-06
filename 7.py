from collections import deque

def maxSlidingWindow(nums, k):
    n = len(nums)
    if n * k == 0:
        return []
    if k == 1:
        return nums

    deq = deque()
    result = []

    for i in range(n):
        if deq and deq[0] == i - k:
            deq.popleft()

        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        deq.append(i)

        if i >= k - 1:
            result.append(nums[deq[0]])

    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))  # Output: [3, 3, 5, 5, 6, 7]

nums = [1]
k = 1
print(maxSlidingWindow(nums, k))  # Output: [1]
