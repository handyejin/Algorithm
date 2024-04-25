def compare_numbers_sum(num1, num2, x):
    s = num1 + num2
    if s == x:
        return 0
    elif s > x:
        return 1
    else:
        return -1


def get_two_pointer(n, array, x):
    array.sort()
    result_cnt = 0
    left = 0
    right = n - 1

    while left < right:
        compare_result = compare_numbers_sum(array[left], array[right], x)
        if compare_result == 0:
            left += 1
            right -= 1
            result_cnt += 1
        elif compare_result == 1:
            right -= 1
        elif compare_result == -1:
            left += 1

    return result_cnt


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())

    print(get_two_pointer(n, arr, x))
