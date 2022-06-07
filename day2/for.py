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

#for문 딕셔너리응용

kang_score ={'수학':80,"영어":70,"과학":60}




        
