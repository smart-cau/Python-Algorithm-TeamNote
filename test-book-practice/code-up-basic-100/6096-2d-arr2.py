# 문제 링크: https://codeup.kr/problem.php?id=6096

if __name__ == '__main__':

    go_arr = [list(map(int, input().split())) for _ in range(19)]

    n = int(input())
    position_arr = [list(map(int, input().split()))for _ in range(n)]

    for a in range(n):
        first_index = position_arr[a][0] - 1
        second_index = position_arr[a][1] - 1

        for b in range(19):
            if go_arr[first_index][b] == 0:
                go_arr[first_index][b] = 1
            else:
                go_arr[first_index][b] = 0
        for b in range(19):
            if go_arr[b][second_index] == 0:
                go_arr[b][second_index] = 1
            else:
                go_arr[b][second_index] = 0

    for i in range(19):
        for j in range(19):
            print(go_arr[i][j], end=' ')
        print()
