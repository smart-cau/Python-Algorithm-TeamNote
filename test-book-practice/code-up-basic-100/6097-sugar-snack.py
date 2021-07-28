# 문제 링크: https://codeup.kr/problem.php?id=6097

if __name__ == '__main__':
    h, w = map(int, input().split())

    n = int(input())
    position_arr = [list(map(int, input().split())) for _ in range(n)]

    go_arr = [[0] * w for _ in range(h)]

    for i in range(n):
        length = position_arr[i][0]
        first_index = position_arr[i][2] - 1
        second_index = position_arr[i][3] - 1
        for j in range(length):
            if position_arr[i][1] == 0:
                go_arr[first_index][second_index] = 1
                second_index += 1
            elif position_arr[i][1] == 1:
                go_arr[first_index][second_index] = 1
                first_index += 1

    for i in range(h):
        for j in range(w):
            print(go_arr[i][j], end=' ')
        print()
