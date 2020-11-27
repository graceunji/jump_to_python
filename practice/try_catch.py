# 8. 예외 처리

def f(a, b):
    try:
        if a and b:
            return (a * b) + (a / b)
        elif a:
            return '불능'
        else:
            return '부정'
    except:
         return '정상적인 값을 입력하시오'
