T = int(input())
for test_case in range(1, T + 1):
	a, b = map(int, input().split())
    #a,b는 a<=b의 관계이며 약수 관계이기에
    #삼각형의 아래에서부터 만들어지는 작은 삼각형을 생각해 보았을때
    #a/b개의 삼각형이 맨 아랫변 그 위로 쌓이는 삼각형의 규칙은
    #a/b = n일때 n-1,n-1,n-2,n-2 ....n-i,n-i의 규칙을 가진다. (n-i)>1 이면 다음과 같은 구현이 나온다.
	answer = a//b
	for i in range(1, a//b):
		answer += 2*(a//b-i)
	print('#'+str(test_case), answer)