# A brief description of the project
# 6 Sept 2018
# CTI-110 P2HW2 - Male Female Percentage
# Veronika Lopez

#Input number of students total in class
students = int(input('How many total students are in the class?'))

#Input number of males
males = int(input('How many males are in your class?'))

#Input number of females
females = int(input('How many females are in your class?'))

#Get percentage of males
Male_ratio = males/students

#Get percentage of females
Female_ratio = females/students

#Show the conversion
print('The percentage of males in the class are',(format(Male_ratio, '%')), '.The percentage of females in the class is',(format(Female_ratio, '%')),'.' )
