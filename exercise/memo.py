# 06-4 간단한 메모장 만들기
'''
원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장을 만들어 보자.

필요한 기능은? 메모 추가하기, 메모 조회하기
입력 받는 값은? 메모 내용, 프로그램 실행 옵션
출력하는 값은? memo.txt

메모 추가는 python memo.py -a "Life is too short" 실행시 메모 추가 가능하도록
'''
import sys

FILE_NAME = 'memo.txt'

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open(FILE_NAME, 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open(FILE_NAME)
    memo = f.read()
    f.close()
    print(memo)



