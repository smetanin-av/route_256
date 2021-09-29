def solve():
    max_rail_len, target_len = map(int, input().split())
    rails_cnt = target_len // max_rail_len
    if target_len % max_rail_len:
        rails_cnt += 1
    print(rails_cnt)


if __name__ == '__main__':
    solve()
