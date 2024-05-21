import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))

    left = 0
    right = 1
    s = arr[0]
    min_length = n

    while left <= right <= n:
        if s < m:
            if right >= n:
                break
            else:
                s += arr[right]
                right += 1
        else:
            # 길이는 right - left
            length = right - left
            if length < min_length:
                min_length = length
            s -= arr[left]
            left += 1

    if sum(arr) < m:
        print(0)
    else:
        print(min_length)
