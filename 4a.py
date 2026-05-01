def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    a, bn=1, 2
    for _ in range(3, n + 1):
        a,b=b, a + b
    return b
n = int(input())
print(climb_stairs(n))
