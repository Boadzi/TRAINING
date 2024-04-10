# A basic calculator that performs basic mathematics operation(+,-,*,/)

print('Welcome to Simple Calculator.')

# Get user input for numbers
number1= float(input('Enter number 1.'))
number2= float(input('Enter number 2.'))

#Get user input for operation 
print('Please select operation.')
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')

users_choice = input('Enter a operation sign. (1,2,3,4):')

if users_choice =='1':
    result = number1+number2
    print(f'Answer is {result}')
elif users_choice =='2':
    result = number1-number2
    print(f'Answer is {result}')
elif users_choice =='3':
    result = number1*number2
    print(f'Answer is {result}')
elif users_choice =='4':
    if number2 == int(0):
        print('Error!')
    result = number1/number2
    print(f'Answer is {result}')