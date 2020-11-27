import time
import threading

def long_task(): # 5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1) # 1초간 대기
        print("working:%s\n" % i)

print("start")

threads =[]
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

print(threads)

for t in threads:
    t.start()

for t in threads:
    t.join() # join으로 스레드가 종료될때까지 기다린다.

print("End")