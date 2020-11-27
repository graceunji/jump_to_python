FILE_NAME = 'input_to_file_test.txt'


while True:
    str = input("그만두기는 end 입력하세요. \n입력해주세요 : ")
    if str == 'end': 
        with open(FILE_NAME, 'r') as f:
            print(f.read())
        break
    else:
        with open(FILE_NAME, 'a') as f:
            f.write(str+"\n")
