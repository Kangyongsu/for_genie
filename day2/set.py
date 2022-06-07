#만약에 리스트에서 중복을 쉽게 제거하고싶다면?

list_1 = [1,1,2,2,3,3]

result = set(list_1)

print(f'result의 값은 {result}입니다')

# result의 모양을 보면 딕셔너리와 굉장히 유사한 모습을 보이고있다.
# 차이점을 캐치해보시오!!

#set에 값추가하기 

for i in range(10):
    print(result)

result.add(3)

print(f'3을 add한후에 result 값은 {result}입니다')

result.add(5)

print(f'5를 add한후에 result 값은 {result}입니다')

result.remove(3)

print(f'remove한후에 result 값은 {result}입니다')