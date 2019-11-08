class Student():
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance
        print("The info about student")

    def get_student_info(self):
        print(self.name + self.lastname + " поступил в "
         + self.year_of_entrance + " году на факультет:" +  self.department  )


student_1 = Student("Вася", " Иванов", "Programming", "2017")
student_1.get_student_info()


