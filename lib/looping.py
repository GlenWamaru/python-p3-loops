#happy new year
def happy_new_year():
    countdown = 10
    while countdown >= 0:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")

happy_new_year()

#square
def square_integers(listof_integers):
    squared_list = []
    for num in listof_integers:
        squared_list.append(num ** 2)
    return squared_list

numbers = [1,2,3,4,5]
numbers_squared = square_integers(numbers)
print(numbers_squared)

#fizzbuzz1
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print ("FizzBuzz")
        elif num % 3 == 0:
            print ("Fizz")
        elif num % 5 == 0:
            print ("Buzz")
        else:
            print(num)

fizzbuzz()
