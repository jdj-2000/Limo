def power(n:int) -> int:
    return n*n

def under_10(n:int)->bool:
    return n <10

#output_map 사용법 테스트
#output_filter 사용업 테스트
def main():
    li = [i+1 for i in range(20)]
    output_map= map(power, li)
    output_filter = filter(under_10, li)
    print("map 의 결과", list(output_map))
    print("filter 의 결과", list(output_filter))

    #람다를 통해서 작성해 보자ㅏㅏㅏㅏ


if __name__ == "__main__":
    main()