# 문제 링크: https://codeup.kr/problem.php?id=6083

if __name__ == '__main__':
    r, g, b = map(int, input().split())
    arr = [r, g, b]
    arr.sort()
    count = 0

    def for_function(x_, num1, num2):
        for y in range(0, num1):
            if y < num2:
                for z in range(0, num1):
                    print(x_, y, z)
                    global count
                    count += 1
            elif y >= num2:
                for z in range(0, num2):
                    print(x_, y, z)
                    count += 1

    for x in range(0, arr[2]):
        if x < arr[0]:
            for_function(x, arr[2], arr[1])
        elif arr[0] <= x < arr[1]:
            for_function(x, arr[2], arr[0])
        elif x >= arr[1]:
            for_function(x, arr[1], arr[0])
    print(count)










