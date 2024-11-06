from collections import deque

def movesToStamp(stamp: str, target: str):
    m, n = len(stamp), len(target)
    s = ['?'] * n
    result = deque()
    queue = deque()
    stamped = [False] * n
    
    target = list(target)
    
    def can_stamp(i):
        return all(s[j] == '?' or s[j] == target[j] for j in range(i, i + m))
    
    for i in range(n - m + 1):
        if can_stamp(i):
            queue.append(i)
            stamped[i] = True

    while queue:
        i = queue.popleft()
        for j in range(m):
            s[i + j] = target[i + j]
        
        result.appendleft(i)  
        
        for k in range(max(0, i - m + 1), min(n - m + 1, i + m)):
            if not stamped[k] and can_stamp(k):
                queue.append(k)
                stamped[k] = True

    return list(result) if s == target else []

stamp = "abc"
target = "ababc"
print(movesToStamp(stamp, target))  

stamp = "abca"
target = "aabcaca"
print(movesToStamp(stamp, target)) 
