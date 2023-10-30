#!/usr/bin/env python
# coding: utf-8

# In[7]:


####........ Assignment........ ####
    
# Part A: 
# Classes in Python
# 1.	Class Definition and Object Creation Create a Python class called "Student" that has the 
# following attributes: name, age, and grade. Define an initialization method to initialize these attributes 
# when an object of the class is created. Create an instance of the class and set the attributes. Finally, 
# print the attributes of the student object.


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


student_1 = Student("Sachin Rajput", 18, 60)
student_2 = Student("Vardan Saini", 16, 68)
student_3 = Student("Vishal Gupta", 15, 40)
student_4 = Student("Rahul Jain", 17, 51)

print("Name:", student_1.name)
print("Age:", student_2.age)
print("Grade:", student_3.grade)



# 2.	Methods in a Class Extend the "Student" class from the previous question. 
# Add a method called "is_passing" that returns True if the student's grade is greater than or equal to 50 and False otherwise. 
# Create an instance of the class and use this method to check if the student is passing. Display the result.


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def is_passing(self):
        return self.grade >= 50

student_1 = Student("Sachin Rajput", 18, 60)
student_2 = Student("Vardan Saini", 16, 68)
student_3 = Student("Vishal Gupta", 15, 40)
student_4 = Student("Rahul Jain", 17, 51)

print("Is the Sachin Rajput passing?", student_1.is_passing())
print("Is the Vardan Saini passing?", student_2.is_passing())
print("Is the Vishal Gupta passing?", student_3.is_passing())
print("Is the Rahul Jain passing?", student_4.is_passing())


class HighSchoolStudent(Student):
    def __init__(self, name, age, grade, school_name):
        super().__init__(name, age, grade)
        self.school_name = school_name


high_school_student_1 = HighSchoolStudent("Deppanushu Gupta", 18, 55, "National Public High School")
high_school_student_2 = HighSchoolStudent("Rahul Maheshwari", 14, 65, "National Public High School")
high_school_student_3 = HighSchoolStudent("Manoj Singh", 17, 65, "National Public School")
high_school_student_4 = HighSchoolStudent("Shubahm Sharma", 16, 65, "National Public High School")



print("Name:", high_school_student_1.name)
print("Age:", high_school_student_2.age)
print("Grade:", high_school_student_3.grade)
print("School name:", high_school_student_4.school_name)




# In[ ]:


# Part B: 


# In[16]:


# Functions in Python
# 4.	Function with Parameters Write a Python function called "calculate_rectangle_area" that 
# takes two parameters, length and width, and returns the area of a rectangle. 
# Call the function with different sets of values and display the results.

def calculate_rectangle_area(length, width):
    area = length * width
    return area


length_1, width_1 = 4, 6
length_2, width_2 = 7, 3

Area_1 = calculate_rectangle_area(length_1, width_1)
Area_2 = calculate_rectangle_area(length_2, width_2)

print("Area of rectangle 1:", Area_1)
print("Area of rectangle 2:", Area_2)


# 5.	Function with Default Parameters Create a Python function called "greet" that 
# takes a name as a parameter and a greeting message as an optional parameter with a default value of "Hello". 
# The function should return a formatted greeting message. 
# Test the function by calling it with and without the optional parameter and display the results.
    
    
def greet(name, greetings ="Hello"):
    formatted_greetings = f"{greetings}, {name}"
    return formatted_greetings

Person_1 = "Ajeet"
Person_2 = "Ramnesh"
formatted_greeting_1 = greet(Person_1, "Hello")
formatted_greeting_2 = greet(Person_2, "Good morning")

print(formatted_greeting_1)
print(formatted_greeting_2)


# 6.	Function with Variable Number of Arguments Write a Python function called "calculate_average" that 
# takes a variable number of arguments and calculates the average of those numbers. 
# Use this function to find the average of 5, 10, 15, and 20, and display the result.

    
def calculate_average(*arguments):
    total = sum(arguments)
    average = total / len(arguments)
    return average


average_result = calculate_average(8, 11, 19, 22)
print("Average:", average_result)


# In[ ]:




