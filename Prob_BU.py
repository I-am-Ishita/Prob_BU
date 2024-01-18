import datetime
# For generating Ticket Number
import random

print('''Welcome to ProbBU,
         For the Bennettians,
         By the Bennettians,
         A Platform for all your University related problems.''')

# Taking Input Student Info
student = ""
room = ""
name = input("Name: \n")


# Check for validation of year
l_year = ["1", "2", "3", "4", "5"]
def valid_year():
    global year
    year = input("Year of Study: \n")
    if(year not in l_year):
        print("Please enter a valid academic year")
        valid_year()
    else:
        pass
valid_year()


course = input("Course Name: \n")
enroll_no = input("Enrollment Number: \n")

# Student is Day Scholar or Hosteller
print('''Enter "H" for Hosteller and "D" for Day Scholar''')


def hosteller_or_day_scholar():
    global student
    student = input()
    if student == "H" or student == "h":
        print("Room Number: ")
        room = input()
    elif student == "D" or student == "d":
        pass
    else:
        print("Enter a valid option.")
        print('''Enter "H" for Hosteller and "D" for Day Scholar''')
        hosteller_or_day_scholar()


hosteller_or_day_scholar()
phone_no = input("Phone Number: \n")

print("---------------------------------------------------------------------------------")

# For Departments
d1 = "IT Department"
d2 = "Finance Department"
d3 = "Maintenance Department"

# if Maintenance Department then following sub departments

sub_d1 = "Furniture"
sub_d2 = "Electrical"
sub_d3 = "Cleaning"

# IT department's sub categories

it_sub1 = "Wi-Fi"
it_sub2 = "Attendance and Fingerprint"
it_sub3 = "Coll-Poll"
it_sub4 = "Codetantra"
it_sub5 = "New Id Card"
it_sub6 = "Others"

# Finance department sub Categories

fin_sub1 = "Fee Receipt"
fin_sub2 = "Balance Fee"
fin_sub3 = "Others"

# Asking the department of Query
department_of_query = ""
print("What Department do you want to raise your query in?")


def enter_department():
    global department_of_query
    if student == "H" or student == "h":
        print('''"1" for "IT Department"
"2" for "Finance Department"
"3" for "Maintenance Department"''')
        department_of_query = input()
        if department_of_query == "1":
            return d1
        elif department_of_query == "2":
            return d2
        elif department_of_query == "3":
            return d3
        else:
            print("Please select a valid query department.")
            enter_department()
    else:
        print('''"1" for "IT Department"
"2" for "Finance Department"''')
        department_of_query = input()
        if department_of_query == "1":
            return d1
        elif department_of_query == "2":
            return d2
        else:
            print("Please select a valid query department.")
            enter_department()

name_of_department = enter_department()
print(name_of_department)

print("---------------------------------------------------------------------------------")


# Asking for category if the selected department is Maintenance when the student is Hosteller

def category_maintenance():
    if department_of_query == "3":
        print("Under what category of Maintenance do you have your query?")
        print('''"1" for "Furniture"
"2" for "Electrical"
"3" for "Cleaning"''')
        global category_of_maintenance_var
        category_of_maintenance_var = input()
        if category_of_maintenance_var == "1":
            return sub_d1
        elif category_of_maintenance_var == "2":
            return sub_d2
        elif category_of_maintenance_var == "3":
            return sub_d3
        else:
            print("Please select a valid category.")
            category_maintenance()


if department_of_query == "3":
    print(category_maintenance())
    print("---------------------------------------------------------------------------------")
else:
    pass


def category_ITdepartment():
    if department_of_query == "1":
        print("Under what category of IT Services do you have your query?")
        print('''"1" for "Wi-Fi"
"2" for "Attendance and Fingerprint"
"3" for "Coll-Poll"
"4" for "Codetantra"
"5" for "Others"''')
        global category_of_It_var
        category_of_It_var = input()
        if category_of_It_var == "1":
            return it_sub1
        elif category_of_It_var == "2":
            return it_sub2
        elif category_of_It_var == "3":
            return it_sub3
        elif category_of_It_var == "4":
            return it_sub4
        elif category_of_It_var == "5":
            return it_sub5
        elif category_of_It_var == "6":
            return it_sub6
        else:
            print("Please select a valid category.")
            category_ITdepartment()


if department_of_query == "1":
    print(category_ITdepartment())
    print("---------------------------------------------------------------------------------")
else:
    pass

# Taking query Input from the student
print(f"Enter your query :")
query = input()

current_time = datetime.datetime.now()

# Current Year
year = current_time.year

# Current Month
month = current_time.month

# Current Day
day = current_time.day

# Current Hours
hour = current_time.hour

# Current Minutes
minute = current_time.minute

# Current Seconds
second = current_time.second

print("Your query has been submitted at ",hour,":",minute,":",second," on ",day,":",month,":",year)

# Generating Ticket Number Of Query
ticket_number = random.randint(300,600)
print("Your Query's Ticket Number for ",name_of_department,"is",ticket_number)
print("Kindly refer to this Ticket Number when visiting the respective Department")

print("---------------------------------------------------------------------------------")

# Query Resolution for Finance Department
if department_of_query == "2":
    print("Your query has been sent to the Finance Department")
    print("Kindly visit the Finance Department on",day+1,":",month,":",year,"Between 8am to 5.30pm")


# Query Resolution for IT Department
if department_of_query == "1":
    print("Your query has been sent to the IT Department")
    if category_of_It_var == "1":
        print("A personal will visit your room",room,"on",day+1,":",month,":",year,"at 15:00:00 to look upon the issue regarding the Wi-Fi.")
    else:
        print("Kindly visit the IT Department on",day+1,":",month,":",year,"Between 8am to 5.30pm")



# Query Resolution for Maintenance Department
if department_of_query == "3":
    if category_of_maintenance_var == "1": # Furniture
        print("Your query has been sent to the Maintenance Department")
        print("A personal will visit your room",room,"on",day+1,":",month,":",year,"at 15:00:00 to look upon the issue regarding the furniture.")
    elif category_of_maintenance_var == "2": # Electrical
        print("Your query has been sent to the Maintenance Department")
        print("A personal will visit your room", room, "on", day + 1, ":", month, ":", year,"at 15:00:00 to look upon the electrical issue.")
    elif category_of_maintenance_var == "3": # Cleaning
        print("Your query has been sent to the Maintenance Department")
        print("A personal will visit your room", room, "on", day + 1, ":", month, ":", year,"at 15:00:00 to clean the room")


print("Thank You!");











