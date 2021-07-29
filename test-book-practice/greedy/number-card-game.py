# 숫자 카드 게임

if __name__ == '__main__':
    n, m = map(int, input().split())
    '''
        교훈 -> 2d list에서 값을 찾을 시, 입력을 받으면서 한 줄씩 값을 검사하는 방법도 있구나
    '''
    # 책 풀이
    result = 0
    ## 한 줄씩 입력받아 확인
    for i in range(n):
        data = list(map(int, input().split()))
        # 현재 줄에서 가장 작은 수 찾기
        min_value = min(data)
        # 가장 작은 수들 중에서 가장 큰 수 찾기
        result = max(result, min_value)
    print(result)

    # # 내 풀이
    # cards = [list(map(int, input().split())) for _ in range(n)]
    #
    # for i in range(n):
    #     cards[i].sort()
    # for i in range(n - 1):
    #     if cards[i + 1][0]:
    #         if cards[i][0] > cards[i + 1][0]:
    #             result = cards[i][0]
    #         else:
    #             result = cards[i + 1][0]
    # print(result)
