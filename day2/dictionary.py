
#딕셔너리 ( 키와 밸류가 존재하는 자료구조)
#딕셔너리의 사용예시 
# 순서가 보장되지 않고 Key값의 중복은 허용하지 않지만 Value값의 중복은 허용된다.

#Q1 스콥스동아리원의 소속과 나이 취미를 나열하시오
user_1 = {"이름": "강용수", "나이": 27, "취미": "일렉기타"}
user_2 = {"이름": "김진희", "나이": 32, "취미": "어쿠스틱기타"}

#Q2 user_1의 이름을 출력하시오
print(f'user_1의 이름은 { user_1["이름"] }입니다.\n')

#Q2 user_1에 졸업유무를 추가하시오
user_1['졸업유무'] = True
print(f'user_1에 졸업유무를 추가한 후에 결과는 { user_1 }입니다.\n')

#Q3 user_1에 졸업유무를 제거하시오

del user_1['졸업유무']
print(f'user_1의 졸업유무를 제거한 후에 결과는 { user_1 }입니다.\n')

#딕셔너리의 키 빌류 추출방법

#키 추출
print(f'user_1.keys()=> {user_1.keys()}')

#강용수라는 값추출
print(f'강용수라는 값을 찾는 식은 user_1[list(user_1.keys())[0]] => {user_1[list(user_1.keys())[0]]}')


#for문을통해서 key값추출
count=1
for i in user_1:
    print(f'{count}번째 key값은 {i}')
    count+=1

count=1
#for문을통해서 value값추출
for i in user_1:
    print(f'{count}번째 value값은 {i}')
    count+=1
