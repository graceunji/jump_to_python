# 4.5 여러 대의 컴퓨터에 연산을 분배하기
# 컴퓨터 n대, 연산프로그램 n개. 가장 최적화 된 프로그램-컴퓨터 분배 수행 하시오.
# pc ; 2대, 프로그램 수행시간은 각각 3, 5, 2 분. 컴퓨터 하나가 3,2 분 수행하고 다른 컴퓨터는 5분짜리.
'''
입력
    computer : 2
    program : 3, 5, 2
출력
    computer1 : 5
    computer2 : 3, 2
'''
# 프로세스 스케줄링 방식 중 LPT(Longest Processing time) 스케줄링.
# 가장 긴 시간을 요하는 job부터 차례대로 가장 적은 업무를 맡은 line에 분배.

def distributeJob(job, com):
    comlist = []
    sumlist = []
    job.sort(reverse=True)

    for c in range(com):
        comlist.append([])
        sumlist.append(0)

    for j in job:
        targetidx = sumlist.index(min(sumlist))
        comlist[targetidx].append(j)
        sumlist[targetidx] += j

    return comlist

if __name__ == '__main__':
    print(distributeJob([3,15,6,22,13,2], 3))


#c = int(input('computer : '))
#pList = list(map(int, input('program : ').split(', '))).sort(reverse=True)

    


