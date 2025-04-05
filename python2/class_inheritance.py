
import test_a
from class_student import Student
#from test_a import print_3_time, print_n_time, print_var


class Graduated_Student(Student):
    def __init__(self, name, korean, math, english, science, art, job, *a, **kwargs):
        super().__init__(name, korean, math, english, science, *a, **kwargs)# super 부모로 올라가서 초기화 수행하고 추가 정의 하는 예제임.
        self.art = art # 추가  art        
        self.job = job #추가 job

    def get_sum(self):
        return self.get_average()*5 - 10

def main():
    park = Student("choi", 43, 63, 64 ,34)
    choi = Graduated_Student("choi", 43, 63, 64 ,34, 50, "teacher")
    print(choi.get_average())
    students = [park, choi]
    for student in students:
        print(student.get_sum())
    # print(choi.get_graduate_sum())
    print(isinstance(choi, Graduated_Student)) # True
    print(isinstance(choi, Student))           # True
    print(isinstance(choi, int))               #false
    print(isinstance(choi,object))                 #int dict list 내장 클래스 예외
    print(isinstance(float,object))
    # True

    print(test_a.print_var)
    test_a.print_3_time()

if __name__ == "__main__":
    main()
    