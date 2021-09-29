def input_int() -> int:
    return int(input())


def test(number: int) -> bool:
    if number < 11:
        return False

    rest = number % 11
    if rest == 0:
        return True

    shift = rest * 111
    return number >= shift and (number - shift) % 11 == 0


def solve():
    length = input_int()
    for _ in range(length):
        number = input_int()
        answer = test(number)
        print('YES' if answer else 'NO')


if __name__ == '__main__':
    solve()
