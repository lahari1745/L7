#write a python program that takes two  numbers from the user and checks if
#1) both the numbers are greater than 10
#2) atleast one of the number is less than 5
#3) the first number is not greater than the second number


x=int(input('x : '))
y=int(input('y : '))

if x>10 and y>10:
  print('both are greater then 10')

else:
    print('both are not greater than 10')

if x<5 or y<5:
  print('atleast one number is less than 5')

else:
    print('neither of the number are less than 5')

if not (x>y):
    print('the first number is not greater than the second number')

else:
        print('the first number is greater tham second number'

              )
