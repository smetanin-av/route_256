"""
В базе данных хранится история значений графика по дням. Каждое значение – это целое число x ≥ 0,
либо специальное значение -1.

Требуется вывести значения точек графика по данным из базы. При этом действуют следующие правила:
    1. если в данных отсутствует значение для дня X или оно равно -1, то текущим считается значение ближайшего
    предыдущего дня, для которого есть значение;
    2. если до дня X нет никаких значений, то в этот день отдаем специальное значение -1, которое говорит о том,
    что данных нет;
    3. для любого дня в будущем отдаем специальное значение -1;

Формат входных данных
На вход в первой строке подаются следующие числа:
    1. номер первого дня графика (включительно) - a ≥ 0;
    2. номер последнего дня (включительно) b ≥ 0, при этом b > a;
    3. номер сегодняшнего дня c;
    4. количество записей в БД 0 < d < 10^5.
Далее следуют данные в формате пар (номер дня, значение), отсортированные в обратном порядке (т.е. сначала идет
последний день, потом остальные). Количество пар может быть не эквивалентно количеству дней, которые будут в графике.

Формат выходных данных
В результате должны присутствовать все дни от первого до последнего включительно в прямом порядке.
"""

from typing import Iterable, Dict


def read_list_of_ints() -> Iterable[int]:
    return map(int, input().split())


def read_graph_values(count: int) -> Dict:
    values = {}
    for _ in range(count):
        day, value = read_list_of_ints()
        values[day] = value
    return values


def solve():
    day_min, day_max, day_now, count = read_list_of_ints()
    values = read_graph_values(count)

    previous = -1
    for day in range(day_min, day_max + 1):
        value = values.get(day, -1)
        if day > day_now:
            print(day, -1)
        elif value != -1:
            previous = value
            print(day, value)
        else:
            print(day, previous)


if __name__ == '__main__':
    solve()
