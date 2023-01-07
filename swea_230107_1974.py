T = int(input())

for test_case in range(1, T + 1):
    x_y = [[0] * 9 for i in range(9)]
    for i in range(9):
        x_y[i] = list(map(int, input().split()))

    # x축 확인
    answer1 = 1
    for i in range(9):
        check = {}
        for j in range(1, 10):
            check[j] = x_y[i].count(j)
        if 0 in check.values():
            answer1 = 0
            break

    # 가로 검증중 중복이 있을시 바로 다음 스도쿠로
    if answer1 != 1:
        print('#' + str(test_case), 0)
        continue

    # y축 확인
    answer2 = 1
    for i in range(9):
        check = {}
        y_list = []
        for j in range(9):
            y_list.append(x_y[j][i])
        for k in range(1, 10):
            check[k] = y_list.count(k)
        if 0 in check.values():
            answer2 = 0
            break

    # 세로 검증중 중복이 있을시 바로 다음 스도쿠로
    if answer2 != 1:
        print('#' + str(test_case), 0)
        continue

    # 33 확인
    answer3 = 1
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = {}
            list_33 = []
            for k in range(3):
                for l in range(3):
                    list_33.append(x_y[k + i][l + j])
            for m in range(1, 10):
                check[m] = list_33.count(m)
            if 0 in check.values():
                answer3 = 0
                break

    print("#{} {}".format(test_case, answer3))