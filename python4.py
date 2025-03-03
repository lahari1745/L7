#ASKING HEIGHT AND WEIGHT TO THE USER AND CALCULATING THE BMI

height = float(input('what is your height? '))
weight = float(input('what is your weight?'))

height = height/100
BMI = weight / height**2
print(f'the BMI is {BMI}')
