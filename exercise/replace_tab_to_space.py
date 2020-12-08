# 06-5 탭을 4개의 공백으로 바꾸기
'''
문서 파일을 읽어서 그 문서 파일 안에 있는 탭(tab)을 공백(space) 4개로 바꾸어 주는 스크립트를 작성해 보자.

필요한 기능은? 문서 파일 읽어 들이기, 문자열 변경하기
입력 받는 값은? 탭을 포함한 문서 파일
출력하는 값은? 탭이 공백으로 수정된 문서 파일

다음과 같은 형식으로 프로그램이 수행되도록 만들 것이다.
python replace_tab_to_space.py src dst
src는 탭을 포함하고 있는 원본 파일 이름
dst는 파일 안의 탭을 공백 4개로 변환한 결과를 저장할 파일 이름
'''
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)

f = open(dst, 'w')
f.write(space_content)
f.close()



