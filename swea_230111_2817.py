def count_k(indx, sum_):
    global answer
    if indx >= n:
        return
    sum_k = sum_ + arr[indx]
    if sum_k == k:
        answer += 1
    count_k(indx + 1, sum_)  # 이전 과정에서 추가로 더해지기 전의 sum을 가져와 증가한 인덱스에 해당하는 값을 더해 확인 ex)1,2,4
    count_k(indx + 1, sum_k)  # 이전 과정에서 추가로 더해진 후의 sum을 가져와 증가한 인덱스에 해당하는 값을 더해 확인    ex)1,2,3,4


T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = 0
    count_k(0, 0)

    print('#' + str(test_case), answer)