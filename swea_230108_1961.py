T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 90도
    arr_90 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr_90[i][j] = arr[n - 1 - j][i]
    # 180도
    arr_180 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr_180[i][j] = arr_90[n - 1 - j][i]
    # 270도
    arr_270 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr_270[i][j] = arr_180[n - 1 - j][i]
    # 출력
    print('#' + str(test_case))
    for i in range(n):
        a_90 = ''.join(map(str, arr_90[i]))
        a_180 = ''.join(map(str, arr_180[i]))
        a_270 = ''.join(map(str, arr_270[i]))
        print(a_90, a_180, a_270)

