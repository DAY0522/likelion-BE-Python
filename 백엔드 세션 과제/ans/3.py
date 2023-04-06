# 3. 

students = {
    '김다영':['코딩', '게임'],
    '부준혁':['춤', '사진'],
    '홍진욱':['잠', '돈']
}

while True:
    print('이름을 입력하세요: ', end='')
    name = input()
    print(students[name])
    print('계속하시겠습니까?(y/n): ', end='')
    if input() == 'n':
        break