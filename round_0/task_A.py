"""
Рулетка Гальтона представляет собой треугольную пирамиду с ячейками (см картинку ниже). На каждой ячейке написано
число - стоимость этой ячейки. Сверху в самую первую ячейку кидают шарик. Шарик из текущей ячейки может равновероятно
скатиться в одну из двух соседних ячеек уровнем ниже. Когда шарик скатывается на самый нижний уровень, подсчитывается
сумма стоимостей всех ячеек, в которых побывал шарик. Эта сумма - выигрыш игрока в казино.

Чтобы казино не разорилось, необходимо контролировать, чтобы средний выигрыш игрока не был слишком большим. Ваша
задача - для данной рулетки Гальтона вычислить средний выигрыш игрока в ней (математическое ожидание). Ответ необходимо
дать в виде несократимой дроби. Если средний выигрыш равен нулю, то ответом считается дробь 0/1.

Ограничения
Высота (количество уровней) рулетки h: 1 <= h <= 63. Значение в одной ячейке - целое число c: -100 <= c <= 100.

Пояснение к примерам:
В первом примере есть два возможных варианта движения шарика — (1, 2) и (1, 3).
Следовательно средний выигрыш = ((1+2)+(1+3))/2 = 7/2

Во втором примере единственный возможный выигрыш = -6. Таким образом ответ -6 1.
Третий пример входных данных изображен на картинке выше. Если подсчитать сумму по всем возможным 4 путям движения
шарика, то получится 9, а значит средний выигрыш - 9 / 4.
"""

import math
from dataclasses import dataclass
from typing import List


def read_int() -> int:
    line = input()
    return int(line)


@dataclass(repr=False, eq=False)
class CellInfo:
    cost: int
    ways: int = 1


def read_next_row() -> List[CellInfo]:
    return [CellInfo(cost=int(x)) for x in input().split()]


def solve():
    count_of_tests = read_int()
    for _ in range(count_of_tests):
        height = read_int()

        prev_row = read_next_row()
        curr_row = prev_row

        for _ in range(1, height):
            curr_row = read_next_row()
            for cell_no, cell in enumerate(curr_row):
                if cell_no == 0:
                    neighbors = (prev_row[cell_no],)
                elif cell_no == len(curr_row) - 1:
                    neighbors = (prev_row[cell_no - 1],)
                else:
                    neighbors = prev_row[cell_no], prev_row[cell_no - 1]
                cell.cost = sum(cell.cost * x.ways + x.cost for x in neighbors)
                cell.ways = sum(x.ways for x in neighbors)
            prev_row = curr_row

        profit = sum(x.cost for x in curr_row)
        if profit != 0:
            count_of_pathes = 2 ** (height - 1)
            gcd = math.gcd(profit, count_of_pathes)
            print(profit // gcd, count_of_pathes // gcd)
        else:
            print(0, 1)


if __name__ == '__main__':
    solve()
