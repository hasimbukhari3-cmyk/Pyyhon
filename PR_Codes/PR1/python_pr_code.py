import datetime

name = input('Enter your name:')
age = input('Ente yur age:')
height = input('Ente your height:')
favorite_number = input('Enter your favorite number:')

#shows the datatype 

print(type(name))
print(type(age))
print(type(height))
print(type(favorite_number))

#type casting

age_i = int(age)
height_f = float(height)
fav_num_i = int(favorite_number)

#current year 

current_year = datetime.date.today().year
birth_year = current_year - age_i

print("current year:",current_year)
print("your birth year:",birth_year)

#T casting 

print(type(age_i))
print(type(height_f))
print(type(fav_num_i))

