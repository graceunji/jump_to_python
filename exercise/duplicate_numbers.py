# 0~9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.
'''

입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
출력 예시: True False False True False

'''


def is_duplicate_numbers(s):
    for n in range(0, 10):
        if s.find(str(n)) == -1 or s.count(str(n)) != 1:
            return False
    return True

print(is_duplicate_numbers('0123456789'))
print(is_duplicate_numbers('01234'))
print(is_duplicate_numbers('01234567890'))
print(is_duplicate_numbers('6789012345'))
print(is_duplicate_numbers('012322456789'))