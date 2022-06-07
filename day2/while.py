#while문 => for문과 동일함

# 현재 나에겐 500원이 남아있습니다
# 0원이 될때까지 나는 15원짜리 사과을 살 계획입니다.
# 1개씩 사면서 특정 조건이 되면 구매를 중지하거나 추매를 할 수 있습니다.
# 0원이 되거나 물건가격보다 적은 돈이 남는다면 구매를 종료합니다.

my_money = 500
apple_price = 15
count= 0

while( my_money >= apple_price): #while문이 true면 아래식을 실행 아니면 탈출
    count += 1
    my_money -= apple_price
    print(f'사과를 {count}개 구매했고 현재 남은돈은 {my_money}입니다.')
   
    
    # 돈이 100원 이하면 구매중지
    # if(my_money<100): 
    #     break;
    
    #사과를 30개를 샀더니 가게주인이 보너스로 1000원을 더 줬다.
    # if(count==30):
    #     my_money +=1000
    #     continue
    
print( f'{my_money}원이 남았고 사과{count}개를 구매했습니다. while문을 종료합니다')

#while의 함정

i=1
while(True):
    print(f"{i}번째루프인데 언제 끝나냐..")
    i+=1
    if(i==40000):break
    

