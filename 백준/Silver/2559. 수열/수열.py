# 2559
def get_prefix_sum_list(input_list):
    prefix_sum_list = [input_list[0]]
    for i in range(1, len(input_list)):
        prefix_sum_list.append(input_list[i] + prefix_sum_list[i - 1])
    return prefix_sum_list


def get_max_sum(prefix_sum_list, k):
    idx = 0
    max_sum = prefix_sum_list[k]
    for i in range(k + 1, len(prefix_sum_list)):
        s = prefix_sum_list[i] - prefix_sum_list[idx]

        if max_sum < s:
            max_sum = s
        idx += 1

    return max_sum


if __name__ == "__main__":
    n, k = input().split()
    inputs = list(map(int, input().split()))

    result = get_prefix_sum_list(inputs)
    print(get_max_sum(result, int(k)-1))
