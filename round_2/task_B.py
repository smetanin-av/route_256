"""
Есть JSON, состоящий из массива объектов, в каждом объекте которого есть поле data. В поле data лежит объект, в котором
гарантируется наличие строкового ключа key`. Длина массива 0 ≤ x ≤ 105.
Требуется посчитать количество уникальных значений среди всех key во всех data.

Формат входных данных
На вход подаётся число 0 < N ≤ 105, далее идут N строк, содержащие в себе JSON файл. Гарантируется, что длина каждой
строки l < 105 символов.

Формат выходных данных
На выход требуется отправить единственное число – количество уникальных ключей во всех data.
"""

import json


def read_single_int() -> int:
    return int(input())


def solve():
    count_or_rows = read_single_int()
    if not count_or_rows:
        print(0)
        return

    text = []
    for _ in range(count_or_rows):
        text.append(input())
    blocks = json.loads(''.join(text))

    keys = set()
    for block in blocks:
        keys.add(block['data']['key'])
    print(len(keys))


if __name__ == '__main__':
    solve()
