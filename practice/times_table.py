# 3.1 함수 - 구구단

def times_table(num):
    for i in range(1,10):
        print(f'{num} * {i} = {num*i}')

if __name__ == '__main__':
    for j in range(2, 10):    
        times_table(j)
