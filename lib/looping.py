#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
        print('Happy New Year!')
happy_new_year()        

def square_integers(int_list):
    square = [n**2 for n in int_list]
    return square

numbers = [1, 2, 3, 4, 5]
ans = square_integers(numbers)
print(ans)

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else: 
            print(num)
