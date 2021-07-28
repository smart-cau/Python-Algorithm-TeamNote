# 문제 링크: https://codeup.kr/problem.php?id=6085

if __name__ == '__main__':
    w, b, h = map(int, input().split())
    bit_size = w * b * h
    to_mb = 2 ** 23
    print("{:.2f}".format(bit_size / to_mb), "MB")  # round()는 소수점이 0이면 생략해버리는 문제... format을 쓰자
