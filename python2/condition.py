def main():
#조건문
    number = int(input(" 숫자를 입력 : "))
    if number % 2 == 0:
        print("짝수 입니다.")
    else:
        print("홀수 입니다.")

#반복문
    for i in range(10):#0 부터 시작  N-1까지 반복        
        print(f"{i} 번쩨 반복하는 문장입니다.")
    print(list(range(10)))#리스트를 통한 객체 보기


if __name__ =="__main__":
    main()   