#for문
#리스트나 문자열의 첫 번째 요소부터 마지막요소까지 반복

#ex1

list_1= [1,2,3,4,5]

#리스트의 길이 
print(f'배열의 길이는 {len(list_1)}입니다\n')

count =0
for i in list_1:
    count+=1
    print(f'{count}번째 반복문일때 i의 값은 list_1[{count-1}]= {i}\n')
    

#for문 + list 응용 (홀짝 필터기)
print(f'range(21)의 출력결과 {list(range(21))}')

odd_number= []
even_number= []

for i in range(21):
    if(i%2 ==0):
        even_number.append(i)
    elif(i%2 ==1):
        odd_number.append(i)
        
print(f'odd_number=> {odd_number}')
print(f'even_number=> {even_number}')


# 질문 (심화단계 어려우시면 스킵!!)

# 딕셔너리와 list의 차이는 무엇이며 이것을 왜 분리하는가?
# 그냥 한곳에 리스트에 넣으면 똑같지않나?

#ex 만약에 고객에 대한 정보를 뽑는다고 해봅시다
members_list = ["yong_su",27,"176cm","genie",32,"180cm"] # [0:3]=> yong_su정보 [3:]=>genie 정보라고 가정

# 이렇게 리스트에 넣어도 문제될것없지만 고객이 100명이라 할때 85번째 고객의 정보를 가져오라면 어떻게할것인가?
# members[254:257] => 얼추 이렇게 될것임

#하지만 딕셔너리를 활용하면 깔끔하게 정리할 수 있음
members_dict = [{"name":"yong_su","age":27,"tall":"176cm"},{"name":"genie","age":32,"tall":"180cm"}]

#이렇게 보면 차이를 잘 이해하기 힘들 수 있으니 예를들어봅시다

#문제1 이름이 yong_su면서 키가 176인 사람을 찾으시오

# members_list 로 푸는방법
user_name = None
user_age  = None
#None = null 값
#null != '' 이 2개는 다름
print()
print(f'null값의 타입은 {type(None)} 입니다.\n')
print(type(''))

for index,value in enumerate(members_list):
    if(index%3==0 and value=='yong_su'): #[::3] 마다 yong_su라는 사람이 있는지 찾음
        user_name = value
    if(index%3==1 and value==27): #[1::3] 마다 27살이 있는지 찾음
        user_age = value
if(user_name!=None and user_age!=None): #
    print("yong_su라는 이름을 가졌으면서 27살인 사람은 존재합니다.")
else:
    print("yong_su라는 이름을 가졌으면서 27살인 사람은 존재하지않습니다.")
    
# members_dict를 이용한 풀이 (리스트와 딕녀서리를 활용한 풀이)

for i in members_dict:
    if(i['name']=='yong_su' and i['age']==27):
        print("yong_su라는 이름을 가졌으면서 27살인 사람은 존재합니다.")
        
#이래도 잘 모르겠다?
#ex 만약에 엑셀에서 A1 = 이름 B1 = 나이 C1= 키로 넣는 상태에서
#                  A1 = 나이 B1 = 키 C1= 이름으로 넣는 순서를 변경한다던가

# 이름 나이 키뿐만 아니라 주소지까지 적어 넣으라고 한다면 list로 구현한 식은 처음부터 다시 작성해야하지만
# 딕셔너리로 작성한 리스트는 유지보수에 매우 용이하다     






        
    
        
    
    
    








        
