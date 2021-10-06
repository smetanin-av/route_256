"""
Однажды на склад привезли сразу несколько партий товаров и выгрузили их в N разных куч, размер каждый кучи a[i].
При этом известно, что в первой куче товары имеют номера от 1 до a[1], во второй от a[1] + 1 до a[1] + a[2] и так далее.
Но из этих товаров надо собрать заказы. Поэтому надо как можно быстрее по номеру товара определять в какой куче он
лежит.

Формат входных данных
В первой строке записано число 0 < N ≤ 10^5 - это количество кучек.
На следующей N целых чисел a[1], a[2], …, a[n]. Причём 1 ≤ a[i] ≤ 10^5, а всего не более чем 10^6 товаров.
Далее на новой строке 1 ≤ M ≤ 10^5 – это количество товаров, которые надо найти.
На последней строке написано M номеров товаров, которые надо найти.

Формат выходных данных
Требуется вывести M строк, каждая из которых содержит номер товара.
"""

from typing import Iterable, List, NamedTuple


def read_list_of_ints() -> Iterable[int]:
    return map(int, input().split())


class HeapInfo(NamedTuple):
    min_code: int
    max_code: int


def find_heap(heaps: List[HeapInfo], code, index_low: int, index_high) -> int:
    heap_no = (index_low + index_high) // 2
    heap = heaps[heap_no]
    if code < heap.min_code:
        return find_heap(heaps, code, index_low, heap_no - 1)
    if code > heap.max_code:
        return find_heap(heaps, code, heap_no + 1, index_high)
    return heap_no


def solve():
    _ = input()
    heaps = []
    min_code = 1
    for heap_no, size in enumerate(read_list_of_ints(), start=1):
        max_code = min_code + size
        heaps.append(HeapInfo(min_code, max_code))
        min_code = max_code + 1

    _ = input()
    first_heap = heaps[0]
    last_heap = heaps[-1]
    for code in read_list_of_ints():
        if first_heap.min_code <= code <= last_heap.max_code:
            heap_no = find_heap(heaps, code, 0, len(heaps) - 1)
            print(heap_no + 1)
        else:
            print(-1)


if __name__ == '__main__':
    solve()
