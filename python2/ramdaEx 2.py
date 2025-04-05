def power(n:int) -> int:
    return n*n

def under_10(n:int)->bool:
    return n <10

#output_map 사용법 테스트
#output_filter 사용업 테스트
def main():
    li = [i+1 for i in range(20)]
    output_map= map(lambda x: x*x, li)#람다로 바꿔서 테스트하는 방법
    output_filter = filter(lambda x:x<10, li)#람다로 바꿔서 테스트하는 방법
    print("map 의 결과", list(output_map))
    print("filter 의 결과", list(output_filter))

    a = lambda x, y : x+ y
    print(a(2,3))

    #람다를 통해서 작성해 보자ㅏㅏㅏㅏ


if __name__ == "__main__":
    main()