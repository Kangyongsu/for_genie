#if문과 함수를 활용한 계산기 만들기

def calculater(num1,num2,operator_type):
    if(operator_type=="+"):
        return num1+num2
    elif(operator_type=="-"):
        return num1+num2
    elif(operator_type=="*"):
        return num1*num2
    elif(operator_type=="/"):
        return num1/num2
    elif(operator_type=="//"):
        return num1//num2
    elif(operator_type=="%"):
        return num1%num2
    
result= calculater(10,3,"/")

print(result)