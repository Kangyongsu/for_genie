#변수선언
#변수란? 하나의 데이터를 저장 할 수 있는 메모리 공간
# 변수는 하나의 문자(a letter)나 밑줄(underscore) 시작해야 한다. 
# 변수의 두번째 문자부터는 문자(letter), 숫자(number) 또는 밑줄(underscore)를 사용할 수 있다. 
# 변수는 대, 소문자을 구분한다. 
# 변수명의 타입은 값에 따라 변화한다. 

a = 1
# a라는 변수는 1이라는 값을 가진다는 의미
print(f' a의값은 {a} 입니다\n')

#변수의 타입종류
#int형
num1 = 100
print(f' num1의타입은 {type(num1)} 입니다\n')

#float(소수형)
float_1= float(10)
print(f' float_1의타입은 {type(float_1)}이고 값은 {float_1} 입니다\n')


#string(문자열)
str1 = '100'
str2 = "100"

print(f' str1의타입은 {type(str1)} 입니다\n')
print(f' str2의타입은 {type(str2)} 입니다\n')
#int와의 차이점은 '' 또는 "" 를 씌우면 문자열로 인식함

#왜 문자열하고 int를 구분하는가?
ex_num = 100
ex_str = '100'

# print(ex_num+ex_str)
# 문자열과 숫자의 합은 실행될 수 없으므로 에러

print(f'int형을 str으로 변환한후에 ex_num 과 ex_str의 합 {str(ex_num)+ex_str}')
print(f'str형을 int으로 변환한후에 ex_num 과 ex_str의 합 {ex_num+int(ex_str)}')

#boolean (참 또는 거짓)

ex_bool_1 = True
ex_bool_2 = False

print(f'ex_bool_1의 타입은 {type(ex_bool_1)}')
print(f'ex_bool_2의 타입은 {type(ex_bool_2)}')
