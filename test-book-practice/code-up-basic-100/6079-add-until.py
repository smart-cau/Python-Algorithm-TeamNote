# 문제 링크: https://codeup.kr/problem.php?id=6079

if __name__ == '__main__':
    num = int(input())
    n = 1
    totalSum = 0
    while num > totalSum:
        totalSum += n
        n += 1
    print(n - 1)
