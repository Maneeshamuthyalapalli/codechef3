T = int(input())
for _ in range (T):
    N = int(input())
    A = list(map(int, input().split()))
    total_people = sum(A)
    rooms_needed = (total_people + 1) // 2
    print(rooms_needed)
