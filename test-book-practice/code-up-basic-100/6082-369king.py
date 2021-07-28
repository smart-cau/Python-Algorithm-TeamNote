# 문제 링크: https://codeup.kr/problem.php?id=6082

if __name__ == '__main__':
    n = int(input())

    def mode3_print(number):
        if number % 3 == 0:
            print("X", end=' ')
        else:
            print(i, end=' ')

    for i in range(1, n+1):
        if i < 10:
            mode3_print(i)
        else:
            mode10 = i % 10
            if mode10 == 0:
                mode3_print(i)
            else:
                mode3_print(mode10)



