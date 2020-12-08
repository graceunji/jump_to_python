# 문자열을 입력받아 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시해 문자열을 압축하여 표시하시오.
'''
입력 예시: aaabbcccccca
출력 예시: a3b2c6a1
'''

def cmprString(string):
    result = ''
    target = ''
    cnt = 1
    for c in string:
        if target != c:
            if target:
                result += target+str(cnt)
            cnt = 1
            target = c
        else:
            cnt += 1
    result += target+str(cnt)
    print(result)


cmprString('aaabbcccccca')

'''

def compress_string(s):
    _c = ""
    cnt = 0
    result = ""
    for c in s:
        if c!=_c:
            _c = c
            if cnt: result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt +=1
    if cnt: result += str(cnt)
    return result

print (compress_string("aaabbcccccca"))  # a3b2c6a1 출력

'''