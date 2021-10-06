"""
Напишите функцию, которая "поворачивает" матрицу N*N, где 0 <= N < 6.

Пример:
rotate_matrix([[1, 2], [3, 4]])

Ответ:
[[3, 1], [4, 2]]
"""

import json
from typing import List

TMatrix = List[List[int]]


def rotate_matrix(matrix: TMatrix) -> TMatrix:
    size = len(matrix)
    return [
        [line[index] for line in reversed(matrix)]
        for index in range(size)
    ]


def solve():
    matrix = json.loads(input())
    answer = rotate_matrix(matrix)
    print(json.dumps(answer))


if __name__ == '__main__':
    solve()
