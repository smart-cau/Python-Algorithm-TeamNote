if __name__ == '__main__':
    repeat = int(input())
    input_arr = list(map(int, input().split()))

    attendance_check_arr = [0 for _ in range(24)]

    # 파이썬은 for in으로 배열을 사용하면 index가 아니라, 배열 값 자체에 접근한다
    for i in input_arr:
        attendance_check_arr[i] += 1

    for j in range(1, 24):
        print(attendance_check_arr[j], end=' ')

