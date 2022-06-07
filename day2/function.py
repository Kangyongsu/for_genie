#함수

#만드는법 def + 함수명 + (매개변수)

#Q1 두수의 합을 만드는 함수를 만드시오

def add_two_num(x,y):
    return x+y

result = add_two_num(1,2)

print(f'add_two_num(1,2)의 결과는 {result}입니다\n')

# 내장함수
# https://docs.python.org/ko/3/library/functions.html

list_1 = [1,2,3,4,5]

print(f'최소값은 {min(list_1)} 입니다. ')
print(f'최대값은 {max(list_1)} 입니다. ')

import math as ma #수학관련된 수식의 모듈을 가져옴

print(f'math모듈을 이용한 5!의 결과는 {ma.factorial(5)} 입니다.' )

list_1.reverse()

print(f'list_1.reverse()후의 결과는 {list_1} 입니다.\n')

list_1.sort()

print(f'list_1.sort()후의 결과는 {list_1} 입니다.\n')

str_1 = '강 용 수 는 펜 더 가 이'
except_space = str_1.split(" ")
print(f'split으로 띄어쓰기를 제거한 배열은 {except_space}입니다')

str_1 = '1,000,000,000'
except_space = str_1.split(",")
print(f'split으로 ,를 기준으로 나눈 배열은 {except_space}입니다')

#예제문제
#어떻게하면 제일 적은 개수의 동전의 개수로 거스름돈을 줄 수 있을까?

def change(n):
    count= 0
    money_type = [500,100,50,10] # 거스름돈의 종류선언
    
    for i in money_type: # 큰 거스롬돈 부터 나눠서 몫만큼 카운트를 증가시키고 나머지에서 2번째 큰 거스롬돈으로 
        count+=n//i
        n=n%i
    print(count)
        
change(1260)