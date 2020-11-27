# 2.4 윤년 판별하기
# 1. 연수가 4로 나눠 떨어지는 해는 윤년. 1988 1992 1996...
# 2. 연수가 4, 100 으로 나눠 떨어지는 해는 윤년이 아님. 1900 2100 2200 2300 2500
# 3. 연수가 4, 100, 400 으로 나눠 떨어지는 해는 윤년 2000 2400

year = int(input('연도를 입력하세요 : '))
year_str = '';

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            year_str = '윤년'
        else:
            year_str = '평년'
    else :
        year_str = '윤년'
else:
    year_str = '평년'

print('{}년은 {}입니다.'.format(year, year_str))
