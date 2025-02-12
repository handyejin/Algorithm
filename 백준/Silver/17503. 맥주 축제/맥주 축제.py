import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
bear = [list(map(int, input().split())) for _ in range(k)]
bear.sort(reverse=True)

l = 0
r = 2**31

while l <= r:
    mid = (l+r) // 2        # 간 레벨

    sum_p = 0               # 먹은 맥주 선호도 합
    drink = 0               # 먹은 횟수
    for p, level in bear:   
        if mid >= level:    # 간 레벨 >= 도수
            sum_p += p
            drink += 1
        if drink == n:      # 먹을 만큼 먹었으면 그만 먹어
            break

    if sum_p >= m and drink == n:   # 선호도, 먹은 횟수 만족하면 값 줄여보기
        r = mid - 1
    else:
        l = mid + 1

if r != 2**31:
    print(l)
else:
    print(-1)