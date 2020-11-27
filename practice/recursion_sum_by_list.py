# 4.1 각 자리 숫자의 합을 구하는 함수(리스트를 이용)
# 재귀함수 x 나눗셈 x 리스트룔 이용.
from functools import reduce

def sumOfDisits(num):
    L = []
    for c in str(num):
        L.append(c)
    return reduce(lambda x, y: int(x) + int(y), L)

if __name__ == '__main__':
    print(sumOfDisits(47253))
