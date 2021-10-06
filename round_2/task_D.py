"""
Есть 0 < N ≤ 10^5 складов. На каждом лежит до 0 < M ≤ 10^5 товаров. У каждого товара свой уникальный числовой артикул
0 < a ≤ 10^5. Некоторые товары могут находиться на нескольких складах одновременно. Для каждого склада известна
стоимость доставки до получателя.

Нужно определить, какую стоимость товара показать пользователю, учитывая его доступность на складе и стоимость доставки.
Разумеется, это должна быть наименьшая из возможных цен.


Формат входных данных
На вход передаются следующие параметры: N - количество складов. Далее в каждой строчке записаны номер склада
0 < W ≤ 10^5, количество разных артикулов товара на нём 0 < C ≤ 10^5, и далее парами артикулы этих товаров a и стоимость
доставки d.
Далее идёт число 0 < M ≤ 10^5 – это количество запросов. После чего идёт M строк, в каждой передаётся артикул товара a и
его цена p.

Формат выходных данных
Требуется вывести в каждой новой строке стоимость доставки товара и номер склада, с которого его доставлять. Если товар
нельзя доставить, то требуется вывести -1 - 1. В случае равенства цен доставки с двух складов вывести склад с наименьшим
номером.
"""

from dataclasses import dataclass
from typing import Iterable, Dict


def read_single_int() -> int:
    return int(input())


def read_list_of_ints() -> Iterable[int]:
    return map(int, input().split())


@dataclass(repr=False, eq=False)
class ItemInfo:
    store_id: int
    delivery: int


def read_next_store_info(items_by_ids: Dict[int, ItemInfo]) -> None:
    store_id, _, *items = read_list_of_ints()
    while items:
        item_id, delivery, *items = items
        item_info = items_by_ids.get(item_id)
        if not item_info:
            items_by_ids[item_id] = ItemInfo(store_id, delivery)
        elif item_info.delivery < delivery:
            continue
        elif item_info.delivery > delivery or item_info.store_id > store_id:
            item_info.store_id = store_id
            item_info.delivery = delivery


def solve():
    count_of_stores = read_single_int()

    items_by_ids = {}  # type: Dict[int, ItemInfo]
    for _ in range(count_of_stores):
        read_next_store_info(items_by_ids)

    count_of_products = read_single_int()
    for _ in range(count_of_products):
        item_id, price = read_list_of_ints()
        item_info = items_by_ids.get(item_id)
        if not item_info:
            print(-1, -1)
        else:
            print(item_info.store_id, item_info.delivery + price)


if __name__ == '__main__':
    solve()
