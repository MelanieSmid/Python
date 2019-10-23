age = 10 #One way statement 
if age == 10:
    print("ten")

name = "Melanie"
if name == "Melanie":
    print("the same")

letter = "C"   #Alphabetical
if letter < "D":
    print("Less than D")

if letter > "B":
    print("Greater than B")

age = eval(input("Enter your age: ")) #Else statment
if age >= 18: 
    print("You are old enough to vote")
else:
    print ("You are not old enough to vote")

year = eval(input("Enter year: ")) #Elif Else IF
if year == 1:
    print ("Freshman")
elif year == 2:
    print ("Sophomore")
elif year == 3:
    print ("Junior")
elif year == 4:
    print ("Senior")
else:
    print("Not a valid year")

VotingAge = eval(input("How old are you? ")) #Multiple conditions
registered = input("Are you registered? (y/n) ")
if VotingAge >= 18:
    if registered == "y":
        print("You are ready to vote!")
    else:
        print("You are not ready to vote.")

ageVote = eval(input("How old are you? ")) #compond conditions
voteRegistered = input("Are you registered? (y/n) ")
if ageVote >= 18 and voteRegistered == "y":
    print("You are ready to vote!")
else:
    print("You are not ready to vote!")

rate = eval(input("what is your hourly wage? "))
hours = eval(input("How many hours did you work? "))
if hours < 40:
    pay = hours * rate
else:
    pay = hours * rate
    overtimeHours = hours - 40
    overtimePay = overtimeHours * (rate * 0.5)
    pay = pay + overtimePay
print("your weekly pay is:", pay)  #comma   

windspeed = eval(input("Enter wind speed in MPH: ")) #Activity Lesson 3
if windspeed < 74:
    print("Not a hurricane")
elif windspeed <= 95:
    print("Category 1 Hurricane.")
elif windspeed <= 110:
    print("Category 2 Hurricane.")
elif windspeed <= 130:
    print("Category 3 Hurricane.")
elif windspeed <= 155:
    print("Category 4 Hurricane.")
else:
    print("Category 5 Hurricane.")