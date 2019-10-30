number = 1
while number <= 5:
    print(number)
    number = number + 1
print("goodbye")

another_number = 1
answer = 'y'
while answer == 'y':
    print(another_number)
    another_number = another_number + 1
    answer = input("Do you want the next number? ")

    for number in range(1, 10, 2):
        print(number)

for numbers in range(5, 0, -1):
    print(numbers)

num_of_nums = eval(input("How many numbers do you want to average? "))
sum = 0.0
for count in range(num_of_nums):
    value = eval(input("Enter a value: "))
    sum = sum + value
average = sum / num_of_nums
print ("The average is:", average)

for numb in range(1, 11):
    if numb == 4:
        break
    print(numb)
print("Thanks!")

for numbs in range(1, 11):
    if numbs == 4:
        continue
    print(numbs)
print("Thanks!")

for the_number in range(1, 11):
    if the_number == 4:
        continue
    print(the_number)
else:
    print("Exited normally")

phrase = input("Enter a phrase: ")
letter = input("Enter a letter: ")
length = len(phrase)

for index in range(0, length):
    if phrase [index] == letter:
        break
else:
    print("Your letter wasn't found")