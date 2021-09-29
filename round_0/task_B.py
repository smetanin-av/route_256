from dataclasses import dataclass
from functools import lru_cache
from typing import List, Iterator


def input_int() -> int:
    line = input()
    return int(line)


class TagsMismatchError(Exception):
    def __init__(self, line: str):
        self.line = line


class TagsMismatchFatal(Exception):
    pass


@dataclass(repr=False, eq=False, frozen=True)
class TagInfo:
    text: str

    @property
    @lru_cache()
    def name(self):
        return self.text.lower().strip('</>')

    @property
    @lru_cache()
    def is_closing(self) -> bool:
        return self.text.startswith('</')

    def is_match(self, other: 'TagInfo') -> bool:
        return self.is_closing != other.is_closing and self.name == other.name


def parse_tags(lines: List[str]) -> Iterator[TagInfo]:
    for line in lines:
        yield TagInfo(text=line)


def process_text_tag(tags_to_read: Iterator[TagInfo], tags_stack: List[TagInfo]) -> None:
    curr_tag = next(tags_to_read)
    if not curr_tag.is_closing:
        tags_stack.append(curr_tag)
        return

    if not tags_stack:
        raise TagsMismatchError(curr_tag.text)

    prev_tag = tags_stack[-1]
    if curr_tag.is_match(prev_tag):
        tags_stack.pop()
        return

    if len(tags_stack) > 1 and curr_tag.is_match(tags_stack[-2]):
        tags_stack.pop()
        tags_stack.pop()
        raise TagsMismatchError(prev_tag.text)

    try:
        next_tag = next(tags_to_read)
    except StopIteration:
        raise TagsMismatchError(curr_tag.text)

    if next_tag.is_match(prev_tag):
        tags_stack.pop()
        raise TagsMismatchError(curr_tag.text)
    raise TagsMismatchFatal()


def solve():
    count_of_docs = input_int()
    for _ in range(count_of_docs):
        count_of_tags = input_int()
        lines = [input() for _ in range(count_of_tags)]
        tags_to_read = parse_tags(lines)
        last_error = None
        tags_stack = []  # type: List[TagInfo]
        has_fatal = False

        while True:
            try:
                process_text_tag(tags_to_read, tags_stack)
            except TagsMismatchError as error:
                if last_error:
                    has_fatal = True
                    break
                last_error = error.line
            except TagsMismatchFatal:
                has_fatal = True
                break
            except StopIteration:
                break

        if has_fatal or len(tags_stack) > 1 or (tags_stack and last_error):
            print('INCORRECT')
        elif tags_stack:
            print(f'ALMOST {tags_stack[0].text}')
        elif last_error:
            print(f'ALMOST {last_error}')
        else:
            print('CORRECT')


if __name__ == '__main__':
    solve()
