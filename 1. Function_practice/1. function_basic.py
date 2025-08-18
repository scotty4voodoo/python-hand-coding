def plus(a: int, b:int) -> int:
    return print(a+b)

def minus(a: int, b:int) -> int:
    return print(a-b)

def multiply(a:int,b:int) -> int:
    return print(a*b)

def divide(a:int,b:int) -> float:
    return print(a/b)

if __name__=="__main__":
    first = int(input("첫번째 숫자를 입력하세요 : "))
    second = int(input("두번째 숫자를 입력하세요 : "))
    op = input("연산자를 입력하세요 (+ , - , *, /) : ")
    
    if op == '+':
        plus(first,second)
    elif op == '-':
        minus(first,second)
    elif op == '*':
        multiply(first,second)
    elif op == '/' and second != 0:
        divide(first,second)
    else:
        print("없는 연산자 이거나, 0으로 나누었습니다.")