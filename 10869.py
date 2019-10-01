a,b = input().split()#두개의 값을 입력받기 위해서 split 사용
i1 = int(a) #각각 받은 a , b 를 나눠서 i1 , i2 변수에 나눠서 배분
i2 = int(b)
def calcu(i1,i2) :#calcu 라는 함수 만듬
    result = ("%d \n%d\n%d\n%d\n%d"%(i1+i2,i1-i2,i1*i2,i1/i2,i1%i2))#계산
    return result
print (calcu(i1,i2))
