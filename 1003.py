i = int (input())#반복할 횟수 정하기
a=[] #0 or 1 값을 받을 리스트 만들기
def fibona(flag):#함수 만들기
        if flag == 0 :#만약 flag 값이 0일때
            a.append(0)#0을 리스트에 넣기
        elif flag == 1:# 함수 만들기
            a.append(1)# 리스트에 1 넣기 
        else :# 뭣도 아니라면
            return fibona(flag-1),fibona(flag-2)#피보나치          
for k in range(i):#반복 i만큼
    flag = int(input())#flag 안에 숫자 넣기
    fibona(flag)#피보나치 실행하기
    print (a.count(0),a.count(1))#0과 1 개수 출력
    del a[:]# 리스트 안에 내용 기초
