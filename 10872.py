i = int(input())#함수 입력 받기
def fact(i):
    if 0 <= i <= 12 : #범위 정해준후 팩토리얼 하
        if i == 1 or i == 0:
           return 1
        else :
            return i*fact(i-1)
print(fact(i))
