# 문제 링크: https://codeup.kr/problem.php?id=6064

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    m1 = a if a < b else b
    m2 = m1 if m1 < c else c
    print(m2)


