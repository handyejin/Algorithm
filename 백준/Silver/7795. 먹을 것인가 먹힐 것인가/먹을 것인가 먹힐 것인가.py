def search_binary(v, b_list):
    start = 0
    end = len(b_list) - 1
    result = -1
    mid = (start + end) // 2

    while start <= end:

        mid = (start + end) // 2

        if v > b_list[mid]:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result


if __name__ == "__main__":
    t = int(input())
    answers = list()
    for _ in range(t):
        s = 0
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        b.sort()

        for value in a:
            s += search_binary(value, b) + 1

        answers.append(s)

    for answer in answers:
        print(answer)