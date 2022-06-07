#비교 연산자

# == (같다)
print(f'1==1 의 결과는 {1==1}')

# !=(같지않다)
print(f'1!=1 의 결과는 {1!=1}')

# a > b (a가 b보다큼 => 초과의 개념 )
print(f'1>1 의 결과는 {1>1}')

# a < b (a가 b보다작음 => 미만의 개념 )
print(f'1<1 의 결과는 {1<1}')

# a >= b (a는 b랑 같거나 b보다크다 => 이상의 개념)
print(f'1>=1 의 결과는 {1>=1}')

# a <= b (a는 b랑 같거나 b보다작다 => 이하의 개념)
print(f'1<=1 의 결과는 {1<=1}')

#EX1
my_age = 33
if(my_age==32):
    print("내 나이는 32살입니다")
elif(type(my_age)==int):
    print(f'my_age의 데이터타입은 {type(my_age)}형입니다')
else:
    print("내 나이는 32살이 아닙니다")

#if(조건식)=> if안에는 결과가 true false둘중에 하나의 결과가 나오는 것만 들어갈 수 있음
#elif는 if문이 false을때 실행되는 구문
#else는 if문과 elif 둘다 false가 나올경우 실행되는 구문

list_1 = [1,2,3,4]

if("1" not in list_1):
    print("list_1에는 문자열 1이 존재하지않습니다")
elif(1 in list_1):
    print("list_1안에는 int형 1인 존재합니다")
#=> 이부분은 for문의 개념을 이해하면 이해하기 쉬우니 넘어가도 됩니다.


#AND OR 사용

if( list_1[0]== 0 or list_1[3]== 4 ):
    print("OR조건이 true")
elif( list_1[0]== 1 and list_1[3]== 4 ):
    print("AND조건이 true")

    

