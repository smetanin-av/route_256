"""
Задача для Python-разработчиков. Напишите функцию, которая переведет число в формат представления, использующийся
в Excel.

Примеры:
`1 -> A`, `2 -> B`, `26 -> Z`, `27 -> AA`, `28 -> AB`

Формат входных данных
На вход функции подается целое число, входящее в диапазон от 1 до 255 включительно.

Формат выходных данных
На выходе должна быть последовательность символов (см. пример)
"""

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
