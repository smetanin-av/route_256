"""
Напишите функцию, которая по строковому пути получает вложенный объект в словаре или списке.

Например:
get_by_dotted_path({'a': {'b': [1, 2]}}, 'a.b.1')

Ответ:
2

При попытке некорректного обращения, например
get_by_dotted_path({'a': {'b': []}}, 'a.c')
нужно выбрасывать `LookupError`.
При пустой строке — возвращать `None`.

Ограничения:
    На вход подаются только словари и списки / их комбинации.
    Все ключи словарей — всегда строки, ключи не должны содержать '.'
    Решение не должно иметь больше трех уровней вложенности.
"""

import json
from typing import Union, List, Dict


def get_by_pathes(container: Union[List, Dict], pathes: List[str]):
    try:
        path = pathes[0]
        value = None
        if isinstance(container, Dict):
            value = container[path]
        elif isinstance(container, List):
            value = container[int(path)]
        rest = pathes[1:]
        return get_by_pathes(value, rest) if rest else value
    except (KeyError, IndexError, NameError):
        raise LookupError()


def solve():
    [container, dotted_path] = json.loads(input())
    if dotted_path:
        try:
            pathes = dotted_path.split('.')
            answer = get_by_pathes(container, pathes)
        except LookupError:
            answer = 'LookupError'
    else:
        answer = None
    print(json.dumps(answer))


if __name__ == '__main__':
    solve()
