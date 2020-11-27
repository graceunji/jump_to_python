# 5.1 클래스 변수

class Family:
    lastname = '김'


def result():
    print('-'*15)
    print("a : ", a.lastname)
    print("b : ", b.lastname)
    print("Family : ", Family.lastname)

    print("a랑 b는 같은 주소인지?",True if id(a.lastname) == id(b.lastname) else False)
    print("a랑 family는 같은 주소인지?",True if id(a.lastname) == id(Family.lastname) else False)
    print("b랑 family는 같은 주소인지?",True if id(Family.lastname) == id(b.lastname) else False)
    print('-'*15)

a = Family()
b = Family()

result()

# 만약, Family.lastname = '박' 하면 a,b lastname이 박으로 변경됨
Family.lastname = '박'
result()

# a.lastname = '이' 로 하면, a.lastname = '이', b.lastname = '박'
a.lastname = '이'
result()

# 이 상태에서 다시 Family.lastname = '최' 하면,
Family.lastname = '최'
result()