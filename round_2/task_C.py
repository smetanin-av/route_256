"""
Есть массив целых чисел, требуется найти в нём самое большое N-ое число.

Формат входных данных
На вход подаётся целое число 0 < M ≤ 10^5, целое число 0 < N ≤ 10^5, разделённые пробелом на первой строке.
На второй строке массив из M целых чисел, разделённых знаком пробел.

Формат выходных данных
Требуется вывести одно число – N-ое самое большое число или -1, если такого числа нет.
"""

from typing import Iterable


def read_list_of_ints() -> Iterable[int]:
    return map(int, input().split())


def solve():
    count, index = read_list_of_ints()
    if not count or not index:
        print(-1)
        return
    values_all = read_list_of_ints()
    uniques = sorted(set(values_all), reverse=True)
    target = uniques[index - 1] if len(uniques) > index else -1
    print(target)


if __name__ == '__main__':
    solve()
