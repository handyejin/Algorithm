import  sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))

    result = 0
    left, right = 0, 1
    s = arr[left]

    while left <= right <= n:
        if s < m:
            if right >= n:
                break
            else:
                s += arr[right]
                right += 1
        elif s == m:
            result += 1
            s -= arr[left]
            left += 1
        elif s > m:
            s -= arr[left]
            left += 1

    print(result)