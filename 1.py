from collections import Counter, deque

def first_unique_char(s: str) -> int:
    char_count = Counter(s)
    
    queue = deque()
    
    for i, char in enumerate(s):
        if char_count[char] == 1:
            queue.append(i)
    
    while queue:
        idx = queue.popleft()
        if char_count[s[idx]] == 1:
            return idx
    
    return -1
print(first_unique_char("leopard"))       # Виведе: 0
print(first_unique_char("loveleopard"))   # Виведе: 2
print(first_unique_char("aabb"))          # Виведе: -1
