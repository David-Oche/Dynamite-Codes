# To write a code that calculates a students CGPA for the number of years spent in the University
print("UNIVERSITY OF NIGERIA, NSUKKA")
input("Enter your faculty: ")
input("Enter your Department: ")
name= input("Enter you full name\n")
input("Enter your Registration/Matric Number: ")
duration=int(input('input the number of years: '))
if(duration>=4):
    while duration>= 1:
        input("Enter your Level: ")
        print("WELCOME TO FIRST SEMESTER")
        offeredCourses=int(input("Enter the number of courses for FIRST SEMESTER: "))
        unit1=0
        gradePoint1=0
        while offeredCourses>=1:
            grade=input("Enter the grade: ").upper()  
            if grade=="A":
                grade=5
                unit=int(input("Enter the unit load for the grade: "))
                gradePoint=unit*grade
                unit1 += unit
                gradePoint1 += gradePoint
            elif grade=='B':
                grade=4
                unit=int(input("Enter the unit load for the grade: "))
                gradePoint=unit*grade
                unit1 += unit
                gradePoint1 += gradePoint
            elif grade=='C':
                grade=3
                unit=int(input("Enter the unit load for the grade: "))
                gradePoint=unit*grade
                unit1 += unit
                gradePoint1 += gradePoint 
            elif grade=='D':
                grade=2
                unit=int(input("Enter the unit load for the grade: "))
                gradePoint=unit*grade
                unit1 += unit
                gradePoint1 += gradePoint
            elif grade=='E':
                grade=1
                unit=int(input("Enter the unit load for the grade: "))
                gradePoint=unit*grade
                unit1 += unit
                gradePoint1 += gradePoint
            elif grade=='F':
                grade=0     
                unit=int(input("Enter the unit load for the grade: "))
                gradePoint=unit*grade
                unit1 += unit
                gradePoint1 += gradePoint
            else:
                print("PLEASE ENTER YOUR CORRECT GRADE") 
            offeredCourses-=1
        print("WELCOME TO SECOND SEMESTER")
        offeredCourses=int(input("Enter the number of courses for SECOND SEMESTER: "))
        unit2=0
        gradePoint2=0
        while offeredCourses>=1:
            grade=input("Enter the grade: ").upper()  
            if grade=="A":
                grade=5
                unit=int(input("Enter the unit load for the grade: "))
                gradePoint=unit*grade
                unit2 += unit
                gradePoint2 += gradePoint
            elif grade=='B':
                grade=4
                unit=int(input("Enter the unit load for the grade: "))
                gradePoint=unit*grade
                unit2 += unit
                gradePoint2 += gradePoint
            elif grade=='C':
                grade=3
                unit=int(input("Enter the unit load for the grade: "))
                gradePoint=unit*grade 
                unit2 += unit
                gradePoint2 += gradePoint
            elif grade=='D':
                grade=2
                unit=int(input("Enter the unit load for the grade: "))
                gradePoint=unit*grade
                unit2 += unit
                gradePoint2 += gradePoint
            elif grade=='E':
                grade=1
                unit=int(input("Enter the unit load for the grade: "))
                gradePoint=unit*grade
                unit2 += unit
                gradePoint2 += gradePoint
            elif grade=='F':
                grade=0     
                unit=int(input("Enter the unit load for the grade: "))
                gradePoint=unit*grade
                unit2 += unit
                gradePoint2 += gradePoint
            else:
                print("PLEASE ENTER YOUR CORRECT GRADE") 
            offeredCourses-=1
        duration-=1
    total_unit = unit1 + unit2
    total_gradePoint = gradePoint1 + gradePoint2
    cgpa = round(total_gradePoint/total_unit, 2)
    print(f"Congratulations %s Your COMMULATIVE GRADE POINT AVERAGE (CGPA) is {cgpa}" %name)
else:
    print("Enter your correct duration of study")