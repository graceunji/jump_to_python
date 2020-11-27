# 3.2 각 자리 숫자의 합을 구하는 재귀 함수
# 어떤 수의 각 자리 숫자의 합을 계산하는 sumOfDigits()를 작성하시오.
# 합살할 숫자가 남지 않을 때 가지 자신을 호출해, 최종적인 합을 구한다.

# 문자열 버전 숫자 앞에서부터 더함
"""
sum = 0

def sumOfDisits(n):
    length = len(n)
    global sum
    sum += int(n) // (10 ** (length - 1))
    if length == 1:
        print(sum)
    else:
        sumOfDisits(n[1:])
    

sumOfDisits(input('숫자를 입력하세요: '))

"""

# 숫자 버전 숫자 뒤에서부터 더함

def sumOfDisits(n):
    if n <= 1:
        return 0
    else:
        return n % 10 + sumOfDisits(n // 10)

if __name__ == '__main__':
    print(sumOfDisits(47253))
