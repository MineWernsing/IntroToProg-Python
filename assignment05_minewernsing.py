# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Mine Wernsing,5/12/2024,Created Script
# ------------------------------------------------------------------------------------------ #

from sys import exit

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
parts: list[str] = []  # Holds the
# list of student data
student_data: dict[str, str] = {}  # one row of student data in a dictionary
students: list[dict[str, str]] = []  # a table of student data.
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Holds the choice made by the user.

# When the program starts, read the file data into a list of dictionaries (table)
try:
    file = open(FILE_NAME, "r")
    for line in file.readlines():
        # Extract the data from the file
        parts = line.strip().split(',')  # split() turns the string into a list
        student_first_name = parts[0]
        student_last_name = parts[1]
        course_name = parts[2]

        # Transform the data from the file
        student_data = {'first_name': student_first_name, 'last_name': student_last_name, 'course': course_name}

        # Load it into our collection (list of dictionaries)
        students.append(student_data)

except FileNotFoundError as e:
    print(f"{FILE_NAME} file not found.")
    print("---Technical Information---")
    print(e, e.__doc__, type(e), sep="\n")

except Exception as e:
    print('Text entered is invalid.')  # Text file not found
    print("---Technical Information")
    print(e, e.__doc__, type(e), sep='\n')

finally:
    if file is not None:
        if not file.closed:
            file.close()

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student_first_name = input("Enter the student's first name: ")
        try:
            if not student_first_name.isalpha():
                raise ValueError("Student first name must be alphabetic.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Student last name must be alphabetic.")
            course_name = input("Please enter the name of the course: ")
            if course_name == "":
                raise ValueError("Course name cannot be an empty string.")
            student_data = {'first_name': student_first_name, 'last_name': student_last_name, 'course': course_name}

            # Load it into our collection (list of dictionaries)
            students.append(student_data)

        except ValueError as e:
            print(e)
            print("---Technical Information")
            print(e, e.__doc__, type(e), sep="\n")

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course']}")
        print("-"*50)

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            for student in students:
                csv_data = f"{student['first_name']},{student['last_name']},{student['course']}\n"
                file.write(csv_data)
            file.close()
        except Exception as e:
            print("---Technical Information")
            print(e, e.__doc__, type(e), sep='n')

        finally:
            if file is not None:
                if not file.closed:
                    file.close()

    # Stop the loop
    elif menu_choice == "4":
        print("Program Ended")
        exit()

    else:
        print("Please only choose option 1, 2, 3 or 4")
