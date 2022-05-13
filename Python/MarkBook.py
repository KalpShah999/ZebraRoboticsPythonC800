class Student:
    def __init__(self, firstName, lastName, mark = "Unassigned", birthday = "Unassigned", studentNumber = "Unassigned", grade = "Unassigned", classNumber = "Unassigned", numberOfClassesAttended = "Unassigned"): 
        self.firstName = firstName
        self.lastName = lastName
        self.mark = mark
        self.birthday = birthday;
        self.studentNumber = studentNumber
        self.grade = grade
        self.classNumber = classNumber
        self.numberOfClassesAttended = numberOfClassesAttended
        
    def setMark(self, mark):
        self.mark = mark
        
    def setBirthday(self, birthday):
        self.birthday = birthday;
        
    def setStudentNumber(self, studentNumber):
        self.studentNumber = studentNumber
    
    def setGrade(self, grade):
        self.grade = grade
        
    def setClassNumber(self, classNumber):
        self.classNumber = classNumber
        
    def setNumberOfClassesAttended(self, numberOfClasses):
        self.numberOfClassesAttended = numberOfClasses
        
    def PrintStudentInformation(self):
        print("Name:", self.firstName + " " + self.lastName)
        print("Student Number:", self.studentNumber)
        print("Grade:", self.grade)
        print("Birthday:", self.birthday)
        print("Mark:", self.mark)
        print("Class Number:", self.classNumber)
        print("Number of Classes Attended", self.numberOfClassesAttended)

kalp = Student("Kalp", "Shah", "98", "September 19, 2003", "660828", "Second Year", "1A", "120")
students = []
students.append(kalp)

while True: 
    menu = input("What would you like to do?\n   1. Add new student\n   2. Update student information\n   3. See Student Information\n   4. Exit\n")
    
    if menu == "1":
        firstName = input("What is the student's first name? ")
        lastName = input("What is the student's last name? ")
        studentNumber = input("What is the student's student number? ")
        birthday = input("What is the student's birthday? ")
        mark = input("What is the student's mark? ")
        grade = input("What is the student's grade? ")
        classNumber = input("What is the student's class number? ")
        classesAttended = input("How many classes has the student attended? ")
        students.append(Student(firstName, lastName, mark, birthday, studentNumber, grade, classNumber, classesAttended))
    elif menu == "2":
        studentNumberToFind = input("What is the student's student number? ")
        for i in students:
            if (i.studentNumber == studentNumberToFind):
                menuOption = input("What would you like to change?\n   1. Grade\n   2. Attendence\n")
                if (menuOption == "1"):
                    newGrade = input("What is the student's new grade? ")
                    i.setGrade(newGrade)
                elif (menuOption == "2"):
                    attendence = input("How many classes has the student attended? ")
                    i.setGrade(attendence)
                else:
                    print("Invalid Option, returning to main menu.")
    elif menu == "3":
        studentNumberToFind = input("What is the student's student number? ")
        for i in students:
            if (i.studentNumber == studentNumberToFind):
                i.PrintStudentInformation()
    elif menu == "4":
        break;
    else: 
        print("Invalid Menu Option")
    