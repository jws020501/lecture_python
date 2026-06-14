n = int(input())
for i in sorted([input().split() for _ in range(n)], key=lambda x: int(x[0])):
    print(*i)