def return_100():
    return 100, 200,"되돌아 가는 문자", True, False;


def main():
    var = return_100()
    a,b, *c = return_100()
    print(type(var))#tuple  임을 확인하려고
    print(var)

    print(a)
    print(b)
    print(c)


if __name__ == "__main__":
    main()