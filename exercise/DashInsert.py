'''
DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤
문자열 안에서 홀수가 연속되면 두 수 사이에 - 를 추가하고,
짝수가 연속되면 * 를 추가하는 기능을 갖고 있다.
DashInsert 함수를 완성하시오.

입력 예시: 4546793
출력 예시: 454*67-9-3
'''


def dashInsert(s):
    n = 0
    result = []
    num_list = list(map(lambda x: int(x), list(s)))
    while n+1 <= len(s)-1:
        result.append(str(num_list[n]))
        is_odd = num_list[n] % 2 == 1
        is_next_odd = num_list[n + 1] % 2 == 1
        if not is_odd and not is_next_odd:  # 짝수연속
            result.append('*')
        elif is_odd and is_next_odd:  # 홀수연속
            result.append('-')
        n += 1
    result.append(str(num_list[n]))
    print("".join(result))


dashInsert('4546793')

'''

data = "4546793"
numbers = list(map(int, data))   # 숫자 문자열을 숫자 리스트로 변경
result = []

for i, num in enumerate(numbers):
    result.append(str(num))
    if i < len(numbers)-1:                   # 다음 수가 있다면
        is_odd = num % 2 == 1                # 현재 수가 홀수
        is_next_odd = numbers[i+1] % 2 == 1  # 다음 수가 홀수
        if is_odd and is_next_odd:           # 연속 홀수
            result.append("-")
        elif not is_odd and not is_next_odd: # 연속 짝수
            result.append("*")

print("".join(result))

'''
