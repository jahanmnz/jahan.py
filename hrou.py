"""second_minute = 60
minute_hour = 60
hour_day = 24 
day_year= 365
 
total_second=second_minute*minute_hour*hour_day*day_year
total_minute=total_second/60
total_hour=total_minute/60
print("this is second to year ",total_second )
print("this is minute to year",total_minute)
print("this is hour to year",total_hour)""


age = 25
if age >=19:
    print("He is a adult ")
else:
    print("He is an minor")"""




def age():
    age = int(input("Enter your age=> "))
    if age < 18:
        print("you are a minor")
    else:
        print("your are an adult")
age()