# 2.5 소수 구하기
# 소수란? 1과 자신으로만 나누어 떨어지는 1보다 큰 자연수.
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ...
# 소수를 구하기 위해서, 2부터 시작하여 각 소수의 배수를 지워나간다.

max_num = int(input('범위 마지막 값을 입력하세요 : '))

numList = list(range(2,max_num));
for i in range(2,max_num):
    for num in numList:
        if num > i and num % i == 0:
            numList.remove(num)

print(numList)

# 첫번째 포문과 나중 포문을 같은 리스트로 해도 상관없다는 사실을 체크 못함
