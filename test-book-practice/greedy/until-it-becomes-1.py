# 1이 될 때까지

if __name__ == '__main__':
    n, k = map(int, input().split())
    result = 0
    '''
        교훈 -> 반복해야하는 내용 중, 가장 많이 반복되는 부분을 한 번에 처리할 수 있도록 머리를 굴려보자
    '''
    # 책 풀이
    while True:
        # n을 k로 나눠 떨어지는 수가 될 때까지 1 씩 한 번에 빼기
        target = (n // k) * k
        result += (n - target)
        n = target
        # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
        if n < k:
            break
        # k로 나누기
        result += 1
        n //= k

    # 마지막으로 남은 수에 대하여 1 씩 빼기
    result += (n - 1)
    print(result)

    # 내 풀이
    result = 0

    while True:
        if n == 1:
            break
        if n % k == 0:
            n /= k
            result += 1
        else:  # 쓸데없이 반복이 제일 많이 일어나는 부분
            n -= 1
            result += 1
    print(result)
