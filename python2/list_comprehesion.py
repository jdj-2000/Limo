def main():
    lil = [i +1 for i in range(100) if i % 2 == 1]# list  에 조건식 for 넣어서 테스트
    print(lil)

    array = ["사과", "자두", "초콜릿", "바나나", "체리"]
    lil2 = [fruit for fruit in array if fruit != "바나나"]
    print(lil2)


if __name__ == "__main__":
    main()