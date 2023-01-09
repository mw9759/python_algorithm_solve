T = int(input())
for test_case in range(1, T + 1):
	d, a, b, f = map(int, input().split())
	#거리 = 속력*시간
    #시간 = 거리/속력
	time = d/(a+b)
    #파리의 이동거리 = 파리속력*시간(기차가 부딪친)
	answer = f*time
	print('#'+str(test_case), answer)