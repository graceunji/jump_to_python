# 05-1 클래스. 사칙연산 클래스 만들기

class calculate:
    def __init__(self, n1=0, n2=0):
        print('기본 계산기 생성')
        self.num1 = n1
        self.num2 = n2
    
    def setdata(self, n1, n2):
        if self.isNum(n1, n2):
            self.num1 = n1
            self.num2 = n2

    def add(self):
        result = self.num1 + self.num2
        self.print_result(result)

    def sub(self):
        result = self.num1 - self.num2
        self.print_result(result)

    def mul(self):
        result = self.num1 * self.num2
        self.print_result(result)

    def div(self):
        if self.num2 == 0:
            print('0으로 나눌 수 없습니다. 값을 다시 입력해주세요.')
        else:    
            result = self.num1 / self.num2
            self.print_result(result)

    def isNum(self, n1, n2):
        if not(str(type(n1)) == "<class 'int'>" or str(type(n1)) == "<class 'float'>"): 
            print(f'첫번째 입력값 {n1}은 숫자가 아닙니다. 값을 다시 입력해주세요.')
            return False
        elif not(str(type(n2)) == "<class 'int'>" or str(type(n2)) == "<class 'float'>"): 
            print(f'두번째 입력값 {n2}은 숫자가 아닙니다. 값을 다시 입력해주세요.')
            return False
        else:
            return True
        
    def print_result(self, result):
        print(result)


# 상속

class myCalculate(calculate):
    def __init__(self, n1=0, n2=0):
        calculate.__init__(self, n1, n2)
        print('내꺼 생성')

    def pow(self):
        result = self.num1 ** self.num2
        self.print_result(result)

    def print_result(self, result):
        # calculate.print_result(self, result)
        print(f'* 결 과 값 * {result}')

c1 = calculate()
c1.setdata(2,1)
c1.add()
c1.sub()
c1.mul()
c1.div()

c2 = myCalculate(2,10)
c2.pow()