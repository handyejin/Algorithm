def get_prefix_sum_list(input_list, length):
    prefix_sum_result = [0] * length
    for idx in range(length):
        if idx == 0:
            prefix_sum_result[idx] = input_list[idx]
        else:
            prefix_sum_result[idx] = input_list[idx] + prefix_sum_result[idx - 1]
    return prefix_sum_result


def get_prefix_sum(ix, jx, prefix_sum_list):
    if ix != 0:
        return prefix_sum_list[jx] - prefix_sum_list[ix - 1]
    else:
        return prefix_sum_list[jx]


if __name__ == "__main__":
    n, m = input().split()
    inputs = list(map(int, input().split()))

    result = get_prefix_sum_list(inputs, int(n))
    m = int(m)
    answers = []
    for idx in range(m):
        i, j = input().split()
        answers.append(get_prefix_sum(int(i)-1, int(j)-1, result))

    for answer in answers:
        print(answer)

