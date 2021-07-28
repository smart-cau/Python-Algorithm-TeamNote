# 문제 링크: https://codeup.kr/problem.php?id=6091

if __name__ == '__main__':
    a, b, c = map(int, input().split())

    day = 1
    while day % a != 0 or day % b != 0 or day % c != 0:
        day += 1
    print(day)

    # 다른 방식으로 3개 이상의 수의 최소 공배수를 구하려 했는데, 생각보다 어렵다 ㅜ
    # arr = [a, b, c]
    # arr.sort()
    #
    # flag = True
    # div = 2
    # result = []
    #
    # while flag:
    #     for i in arr:
    #         arr

