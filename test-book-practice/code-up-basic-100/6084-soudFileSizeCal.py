# 문제 링크: https://codeup.kr/problem.php?id=6084

if __name__ == '__main__':
    h, b, c, s = map(int, input().split())
    bit_size = h * b * c * s
    division_number = 2 ** 23
    print(round(bit_size/division_number, 1), "MB")
