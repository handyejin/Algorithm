def binary_search(input_list):
    start = 0
    end = len(input_list) - 1

    sum_abs = abs(input_list[start] + input_list[end])

    mid = (start + end) // 2
    answer_start, answer_end = start, end
    while start < end:
        mid = (start + end) // 2
        s = input_list[start] + input_list[end]
        if s == 0:
            return input_list[start], input_list[end]

        if abs(s) <= sum_abs:
            sum_abs = abs(s)
            answer_start = start
            answer_end = end
        if s > 0:
            """
            if end == mid:
                end = mid -1
            else:
                end = mid
            """
            end = end - 1
        else:
            """
            if start == mid:
                start = mid + 1
            else:
                start = mid
            """
            start = start + 1

    return input_list[answer_start], input_list[answer_end]


if __name__ == "__main__":
    n = int(input())
    inputs = list(map(int, input().split()))
    inputs.sort()
    s, e = binary_search(inputs)

    print(f'{s} {e}')
