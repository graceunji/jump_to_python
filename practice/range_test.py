# 2.6 for - 화학 실험
# 프로그램은 최소/최대 안전온도를 나타내는 두개의 정수를 읽음
# 화학 반응 완료시, 장치는 끝을 알리는 -999 보낸다.
# 기록된 온도가 올바른 범위 내 있을 경우(최소값<=온도<=최대값) nothing to report 표시
# 범위내가 아니라면 장치가 온도값을 계속 보내더라도 alert! 표시하고 중

# input은 최소/최대값, 온도 리스트 (마지막은 -999 여야함)

MIN, MAX = map(int, input('최소 온도와 최대 온도를 입력하세요 : ').split())
L = map(int, input('온도 리스트를 입력하세요 : ').split())

for t in L:
    if t == -999:
        break
    elif t < MIN or t > MAX:
        print('Alert!')
        break
    else:
        print('Nothing to report')
                
