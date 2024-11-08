# VARIABLES

grades = []
num_student = 1
students_passed = 0 
total = 0
loop = True

# INPUT GRADES

while loop == True:
        grade_input = input(f"\nEnter the grade for Student {num_student}: ")
        if grade_input.replace(".", "", 1).isdigit() and grade_input.count(".") <= 1:
            grade_input = float(grade_input)
            if grade_input >= 40 and grade_input <= 100:
                grades.append(grade_input)
                num_student += 1
                continue
            else:
                print("Error: Invalid input (must be between 40 and 100). Try again.")
                continue
        elif grade_input.upper() == "DONE":
            loop = False
        else:
            print("Error: Invalid input. Please enter a valid number.")
            continue
        
else:
    
    if grades != []:
        for studgrade in grades:
            total += studgrade
            average_grade = total / len(grades)
        else:
            print(f"\n~.~.~.~.~""\n \nThe average grade of the students: {average_grade:.2f}")
        for studgrade in grades:
            if studgrade >= 75:
                students_passed += 1
        else:
            print(f"\nNumber of students who passed: {students_passed}")
            passing_percentage = (students_passed / len(grades)) * 100
            print(f"\nPassing percentage: {passing_percentage:.2f}%")
            
    else:
        print("No grades were entered.")
