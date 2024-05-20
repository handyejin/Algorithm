import sys


def get_prefix_sum(arr, n):
    prefix_sum_arr = [0] * (n+1)
    for i in range(n):
        prefix_sum_arr[i + 1] = arr[i] + prefix_sum_arr[i]

    return prefix_sum_arr


# 구간별 합 구하기
def get_partial_sum(prefix_sum_arr, m):
    count = 0
    for i in range(1, len(prefix_sum_arr)):
        if prefix_sum_arr[i] == m:
            count += 1
        else:
            for j in range(i-1, 0, -1):
                if prefix_sum_arr[i] - prefix_sum_arr[j] == m:
                    count += 1
                    break
    return count

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))

    prefix_sum_arr = get_prefix_sum(arr, n)
    count = get_partial_sum(prefix_sum_arr, m)
    print(count)


