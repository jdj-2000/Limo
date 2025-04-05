def print_n_times(n : int, *value):   #힌트를 주기 위해 : int   줄 수 있다.
    """
    Args:
        n (int): 반드시 인트로 넣으세요.
    """
    print(type(value))#튜플로 동작 한다는 것을 확인하고자 출력 해봄.
    #for i in range(n):
    for _ in range(n):#윗 줄과 비교,, 안쓰는 변수는 "_"  로 표시할 수 있음,.
        for v in value:
            print(v)
        print()

def print_n_times_default(value, n=3):
    for _ in range(n):
        print(value)


def print_n_times_keyword(value, *values, a=3, b=4, c=5):
    for _ in range(a):
        print(a,b,c)
        print(value)
        for v in value:
            print(values)


#가변 키워드 매개 변수
def print_n_times_keyword_varible(value, *values, a=3, b=4, c=5, **kwargd):
    print(type(kwargd)) #dictionary
    for _ in range(a):
        print(a,b,c)
        print(value)
        for v in values:
            print(values)
    for k, v in kwargd.items():
        print(k,v)



def main():
    print_n_times(3, "abc", "def", "안녕", "하세요.")
    print_n_times_default("안녕하세요.")
    print()
    print_n_times_default("안녕하세요.", 5)
    print()
    print_n_times_keyword("안녕하세요.", 5, "abc", "def")
    print()
    print_n_times_keyword("안녕하세요.", 5, "abc", "def",a=6, b=7)
    print_n_times_keyword_varible("안녕하세요.", 5, "abc", "def",a=6, b=7, new="new 의 값")
    


if __name__ == "__main__":
    main()