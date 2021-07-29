# 큰 수의 법칙

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))

    # 책 풀이 2 -- 권장 -> m이 10억 이상 등 큰 수일 때도 적용 가능한 방법
    '''
        교훈 -> 풀이 과정에서 수열의 규칙을 찾아보기
    '''
    data.sort()
    first = data[n - 1]
    second = data[n - 2]
    # 내 풀이
    result = (first * k + second) * (m // (k + 1)) + first * (m % (k + 1))

    # 책 풀이
    count = int(m / (k + 1)) * k
    count += m % (k + 1)

    result = 0
    result += count * first
    result += (m - count) * second

    print(result)
'''
    # 책 풀이 1
    data.sort()
    first = data[n - 1]
    second = data[n - 2]

    result = 0

    while True:
        for i in range(k):
            if m == 0:
                break
            result += first
            m -= 1
        if m == 0:
            break
        result += second
        m -= 1

    print(result)

    # 내 풀이
    data.sort(reverse=True)

    result = 0
    count = 0

    for i in range(m):
        count += 1
        if count <= k:
            result += data[0]
        elif count > k:
            result += data[1]
            count = 0

    print(result)
'''


