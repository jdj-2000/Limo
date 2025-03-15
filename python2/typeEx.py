def main():
    abc = 4 #abs --class of int -> object
    print(abc, type(abc))
    abc = 4.5
    print(abc, type(abc))
    abc = "this is string"
    print(abc, type(abc))

    abc = "fstring"
    number = 3.141592
    #format -- f-string
    print(f"string string {abc} pi : {number:.3}") # 

if __name__ == "__main__":
    main()
