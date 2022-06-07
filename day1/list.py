#리스트
# 자료를 한 줄로 저장해놓은 자료구조 => 그냥 집합이라 생각하시면 편합니다

list_1 = [1,2,3,4,5]
print(f'list_1의 타입은 {type(list_1)}이고 값은 {list_1}입니다')

list_2 = [1,"2",3,True,5.3]
print(f'list_1의 타입은 {type(list_2)}이고 값은 {list_2}입니다\n')
#위와 같이 어려가지 타입이 들어 갈 수 있습니다.

#리스트의 인덱싱예시
#Q1 강용수의 인적사항을 나열하시오
kang_score = ['1996-07-09','176cm','경영학부','18학점']

#Q2 강용수의 생년월일을 출력하시오
print(f'강용수의 생년월일은 {kang_score[0]} 입니다\n')

#Q3 강용수의 학점을 출력하시오
print(f'강용수의 학점은 {kang_score[3]} 입니다')
print(f'강용수의 학점은 {kang_score[-1]} 입니다\n')

#Q4 강용수의 키와 학부를 출력하시오
print(f'강용수의 키와 학부는은 {kang_score[1:3]} 입니다')
print(f'강용수의 키와 학부는은 {kang_score[1]} , {kang_score[2]} 입니다\n')

#Q4 강용수의 생년월일과 학부를 출력하시오
print(f'강용수의 생년월일과 학부는 {kang_score[::2]} 입니다\n')

#Q5 강용수에 false를 추가하시오 
kang_score.append(False)

print(f'강용수이 false를 추가한 값 {kang_score}\n')

#Q6 강용수에 false를 제거하시오
kang_score.remove(False)

print(f'강용수이 false를 제거한 값 {kang_score}\n')


#문자열에서도 똑같이 적용됨

str = '강용수는펜더가이'
print(f'str[0]=> {str[0]}')
print(f'str[1:4]=> {str[1:4]}')
print(f'str[5:]=> {str[5:]}')

#count ,find 함수
print("'강'의 위치",str.find("강")) #0번째 인덱스에 강이 존재하니까 0이출력
print("'강'의 개수",str.count("강")) #강은 총 1개가 존재하므로 1가나옴


