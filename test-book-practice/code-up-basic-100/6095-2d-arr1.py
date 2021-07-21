if __name__ == '__main__':

    n = int(input())

    white_list = [list(map(int, input().split())) for _ in range(n)]

    go_arr = [[0] * 20 for _ in range(20)]

    for w in range(n):
        first_index = white_list[w][0]
        second_index = white_list[w][1]
        go_arr[first_index][second_index] = 1

    for i in range(1, 20):
        for j in range(1, 20):
            print(go_arr[i][j], end=' ')
        print()

