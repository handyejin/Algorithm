def binary_search(data, target):
    start = 0
    end = data[-1]
    mid = (start + end) // 2

    while start < mid < end:

        sum_list = sum_money(mid, data)
        # print(f'{start} | {end} | {mid}: {sum_list}')

        if sum_list == target:
            return mid
        # 예산 초과
        if sum_list > target:
            end = mid
        else:
            start = mid
        mid = (start + end) // 2

    return mid


def sum_money(mid, data_list):
    s = 0
    for data in data_list:
        if data < mid:
            s += data
        else:
            s += mid
    return s


if __name__ == "__main__":
    n = int(input())
    inputs = list(map(int, input().split()))
    m = int(input())

    inputs.sort()
    if sum(inputs) <= m:
        print(inputs[-1])
    else:
        result = binary_search(inputs, m)
        print(result)
