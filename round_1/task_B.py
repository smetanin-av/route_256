"""
Напишите функцию, которая возвращает все варианты комбинаций членов списков, переданных на вход.

Пример:
pairwise([1, 2, 3], ['a'], [True, False]) = [
    [1, 'a', True],
    [1, 'a', False],
    [2, 'a', True],
    [2, 'a', False],
    [3, 'a', True],
    [3, 'a', False]
]
"""

import json
from typing import List


def pairwise(*lists: List) -> List:
    if not lists:
        return []
    if len(lists) == 1:
        return lists[0]

    first, second, *others = lists
    result = [[val0, val1] for val0 in first for val1 in second]

    while others:
        next_list, *others = others
        result = [
            [*row, val]
            for row in result
            for val in next_list
        ]
    return result


def solve():
    lists = json.loads(input())
    answer = pairwise(*lists)
    print(json.dumps(answer))


if __name__ == '__main__':
    solve()
