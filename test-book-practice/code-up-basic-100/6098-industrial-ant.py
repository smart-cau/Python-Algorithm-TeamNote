# 문제링크: https://codeup.kr/problem.php?id=6098

if __name__ == '__main__':
    ant_nest = [list(map(int, input().split())) for _ in range(10)]

    stuck = False
    found = False

    first_index = 1
    second_index = 1

    while not stuck and not found:
        ant_nest[first_index][second_index] = 9
    # 오른 쪽 우선 탐색
        if ant_nest[first_index][second_index + 1] == 0:
            second_index += 1
            ant_nest[first_index][second_index] = 9

        # 오른쪽이 막히면, 아래 쪽 탐색
        elif ant_nest[first_index][second_index + 1] == 1:
            if ant_nest[first_index + 1][second_index] == 0:
                first_index += 1
                ant_nest[first_index][second_index] = 9
            elif ant_nest[first_index + 1][second_index] == 2:
                first_index += 1
                ant_nest[first_index][second_index] = 9
                found = True
            elif ant_nest[first_index + 1][second_index] == 1:
                stuck = True
        elif ant_nest[first_index][second_index + 1] == 2:
            second_index += 1
            ant_nest[first_index][second_index] = 9
            found = True

    for i in range(10):
        for j in range(10):
            print(ant_nest[i][j], end=' ')
        print()
