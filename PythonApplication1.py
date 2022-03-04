def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x* y

def divide (x,y):
    return x / y

print('Calculator')
print('\nSelcet option:')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')

while True:
    choice=input('Enter Choice 1/2/3/4:')
    num1=float(input("Enter Number1:"))
    num2=float(input("Enter Number2:"))

    if choice == '1':
        print(num1, "+", num2, '=' , add(num1,num2))

    elif choice =='2':
         print(num1, "-", num2, '=' , subtract(num1,num2))
         
    elif choice =='3':
         print(num1, "*", num2, '=' , multiply (num1,num2))
     
    elif choice =='4':
         print(num1, "/", num2, '=' , divide (num1,num2))

    next_cal = input("\nContinue? (yes/ no)")
    if next_cal =='no' :
        break
else:
    print('Invalid Option')