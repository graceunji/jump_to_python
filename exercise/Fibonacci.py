# 입력을 정수 n으로 받았을 때, n 이하까지의 피보나치 수열을 출력하는 함수를 작성해 보자.

def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    return fibonacci(n-1)+fibonacci(n-2)

for i in range(10):
    print(fibonacci(i), end=' ')