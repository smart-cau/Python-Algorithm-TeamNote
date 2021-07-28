# 문제 링크: https://codeup.kr/problem.php?id=6070

if __name__ == '__main__':
    month = int(input())

    # 때때로 수들의 특징을 관찰하고, 이용하면 매우 간단히 해결할 수도 있다.
    if month == 12:
        print("winter")
    elif month == 1 or month == 2:
        print("winter")
    elif month // 3 == 1:
        print("spring")
    elif month // 3 == 2:
        print("summer")
    elif month // 3 == 3:
        print("fall")
