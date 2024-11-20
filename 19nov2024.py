# p1.Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         area = 3.14 * radius**2
#         return area

#     def circumference(self):
#         return 2 * 3.14 * radius

# radius = int(input())
# circle = Circle(radius)
# print(circle.area)
# print(circle.circumference())

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# p2.Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
year, month, day = map(int, input("separate birthdate's Y-M-D with '-'").split("-"))
presentyear, presentmonth, presentday = map(int, input("separate today's Y-M-D with '-'").split("-") 
)

class Dateofbirth:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    


class Person:
    def __init__(self, name, country, dateofbirth):
        self.name = name    
        self.country = country
        self.dateofbirth = dateofbirth

    def age(self):
        ageyear = presentyear - year
        if presentmonth >= month:
            agemonth = presentmonth - month
        else:
            ageyear -= 1
            agemonth = month - presentmonth

        if presentday >= day:
            ageday = presentday - day
        else:
            ageday = 30 - (day - presentday)
            if agemonth > 0:
                agemonth -= 1
            elif agemonth <= 0:
                ageyear -= 1
        return(ageyear, agemonth, ageday)


person = Person("ayachi", "india", year, month, day)

print(person.age())

    




