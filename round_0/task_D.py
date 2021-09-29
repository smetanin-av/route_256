import json


def input_int() -> int:
    return int(input())


def to_excel_format(number: int) -> str:
    digits = []
    while number:
        number -= 1
        digit = chr(ord('A') + number % 26)
        digits.insert(0, digit)
        number //= 26
    return ''.join(digits)


def solve():
    answer = to_excel_format(input_int())
    print(json.dumps(answer))


if __name__ == '__main__':
    solve()
