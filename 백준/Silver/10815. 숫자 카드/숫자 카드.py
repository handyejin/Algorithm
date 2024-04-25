def binary_search(target, data):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if target == data[mid]:
            return True

        if target <= data[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return False


if __name__ == "__main__":
    n = int(input())
    card_list = list(map(int, input().split()))

    m = int(input())
    answer_list = list(map(int, input().split()))

    card_list.sort()
    for answer in answer_list:
        is_exist = binary_search(answer, card_list)
        if is_exist:
            print('1', end=' ')
        else:
            print('0', end=' ')
