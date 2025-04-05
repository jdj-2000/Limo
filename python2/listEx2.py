def main():
    list_a = [1,2,3]
    list_b = [4,5,6]
    print(list_a + list_b)# 더하기 1,2,3,4,5,6

    print(list_a*3)# 곱하기 인데,,,, 1,2,3,1,2,3,1,2,3 반복
    list_a.append("추가원소")#type : ignore
    print(list_a)
    list_a.insert(1, "insert 추가원소")#type : ignore
    print(list_a)

    del list_a[2]
    print(list_a)

    list_a.pop(1)
    print(list_a) 

    list_a.remove(3)
    print(list_a)

if __name__ == "__main__":
    main()