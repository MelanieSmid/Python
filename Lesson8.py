# Lesson 8 List structure basics

days_of_week = ['Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat']

print(days_of_week [2])

for count in range (len(days_of_week)):
    print(days_of_week[count])

days_of_week[0] = 'Sunday'

print(days_of_week)
print(days_of_week [2:5])

# append

my_list = [] 

my_list.append(10)
my_list.append('ten')
print(my_list)

# extend

my_list.extend ([20, 'twenty'])
print(my_list)

# concatenation

my_list = my_list + [30, 'thirty']

# insert

my_list.insert(3, 'hi there!')
print(my_list)

# remove

my_list.remove('hi there!')
print(my_list)

my_numbers = [32, 432, 53, 5, 632, 43, 9]
print( max(my_numbers))

my_list.reverse()
print(my_list)