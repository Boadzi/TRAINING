# create a simple project where we manage a student database using dictionaries and lists. We'll have a dictionary for each student, containing their name, age, and a list of courses they're enrolled in.

students_database = {}

# adding new student
def students(name,age):
 students[name] = {"age": age, "courses": []}

 # enrolling student
 def enroll_students(name,course):
    if name in students:
        students[name]["courses"].append(course)
    else:
        print(f"Student '{name}' not found!")    