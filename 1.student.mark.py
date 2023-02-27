#Define the function
    #Input the number of student
def number_student(n):
    n = int(input("Enter the number of student:\nn = "))
    for i in range(1, n+1, 1):
        print("Information of the {0} student is: ".format(i))
        listStudents.append(student_information(id, name, DoB))
    return listStudents
    #Input the number of course
def number_course(m):
    m = int(input("Enter the number of course:\nm = "))
    for i in range(1, m+1, 1):
        print("Information of the {0} course is: ".format(i))
        listCourses.append(course_information(id, name))
    return listCourses
    #Input student information
def student_information(id, name, DoB):
    id = input("Student ID: ")
    name = input("Student Name: ")
    DoB = input("Student DoB: ")
    return {"id": id , "name": name , "DoB": DoB}
    #Input course information
def course_information(id, name):
    id = input("Course ID: ")
    name = input("Course Name: ")
    return {"id": id , "name": name}
#------------------------------------------
def mark_information(id, name, mark):
    return {"id": id, "name": name, "mark": mark}
#------------------------------------------
#Truy van tu ham khac di vao(QUAN TRONG CAN NHO)
def input_mark(listStudents, listCourses, marks, mark):
    print("Mark of the course of the students is: ")
    for i in range(0, len(listCourses), 1):
        print("{0}: ".format(listCourses[i]['name']))
        
        for j in range(0, len(listStudents), 1):
            mark = int(input("{0} mark: ".format(listStudents[j]['name'])))
            #---------------
            id = listStudents[j]["id"]
            name = listCourses[i]["name"]
            #---------------
            marks.append(mark_information(id, name, mark))
    return marks
#------------------------------------------
def show_mark(course):
    course = input("Choose course you want to show mark: ")
    for k in range(0, len(marks), 1):
        if course == marks[k]['name']:
            for j in range(0, len(listStudents), 1):
                print("{0} mark of {1} is: {2}".format(marks[k]['name'] , listStudents[j]['name'] , marks[k]['mark']))
                break
    return 1
#------------------------------------------
#Declare variable
n = 0 
m = 0
id = ""
name = ""
DoB = ""
course = ""
#-----------
marks = []
mark = 0
#-----------
#Declare the empty list
listStudents = []
listCourses = []
#Solving the problem
number_student(n)
print("--------------------")
number_course(m)
print("--------------------")
input_mark(listStudents, listCourses, marks, mark)
print("--------------------")
show_mark(course)





   
    
    
