#write a program which estimates a users typical food expenditure.
#the program asks the user how many times a week they eat at the student cafeteria .
#then it asks for the price of a typical student lunch, and money spent on groceries during the week.
#based on this information calculate the typical food expenditure both weekly and daily.

cafeteria_meals=int(input('how many times a week do you eat at the student cafeteria? : '))
lunch_price= float(input('the price of a typical student lunch is (in RS): '))
groceries_cost=float(input('money spent on the groceries per week is(in Rs): '))

weekly_expenditure= (cafeteria_meals * lunch_price )+ groceries_cost
daily_expenditure= weekly_expenditure/7
    
print('\nAverage food expenditure: ')
print(f'Weekly : {weekly_expenditure}')
print(f'Daily: {daily_expenditure}')
