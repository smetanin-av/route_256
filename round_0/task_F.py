def solve():
    boxes_count = int(input())
    weights = sorted(map(int, input().split()), reverse=True)

    apples_count = 0
    for index in range(0, boxes_count, 2):
        apples_count += weights[index] - weights[index + 1]

    print(apples_count)


if __name__ == '__main__':
    solve()
