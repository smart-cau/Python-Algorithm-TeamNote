# 문제 링크: https://codeup.kr/problem.php?id=6081

if __name__ == '__main__':
    n = int(input(), 16)

    for i in range(1, 16):
        print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='') # x -> 소문자 출력 / X -> 대문자 출력
