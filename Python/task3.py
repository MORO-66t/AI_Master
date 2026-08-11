def mul(num1 : int,num2 : int )-> int:
    '''
    mul: multiply two numbers

    :param num1: number1
        :type num1: integer

    :param num2: number2
    :type num2: integer

    :return: result of multiplication
    '''
    return num1*num2
def div(num1,num2):
    '''
    div: divide two numbers

    :param num1: number1
    :type num1: integer

    :param num2: number2
    :type num2: integer

    :return: result of division
    '''
    if num2==0:
        return "Can not devide by zero"
    else:
        return num1/num2
def add(num1,num2):
    '''
    add: add two numbers

    :param num1: number1
    :type num1: integer

    :param num2: number2
    :type num2: integer

    :return: result of addition
    '''
    return num1+num2
def sub(num1,num2):
    '''
    sub: subtract two numbers

    :param num1: number1
    :type num1: integer

    :param num2: number2
    :type num2: integer

    :return: result of subtraction
    '''
    return num1-num2    




def calculator ():
    '''
    calculator: calculator menu

    :return: calculator menu
    '''
    print(" 1.add \n 2.sub \n 3.mul \n 4.div")
    choice=input("Enter your choice :")
    if choice == "1"or choice == "2" or choice == "3" or choice == "4":
        while True:
            try:
                num1=input("Enter the first number :")
                num1=int(num1)
                num2=input("Enter the second number :")
                num2=int(num2)
                break
            except:
                print("invalid number")

        
    else:
        print("Invalid choice")
        calculator()

    if choice=="1":
        answer =add(num1,num2)
    elif choice=="2":
        answer =sub(num1,num2)
    elif choice=="3":
        answer =mul(num1,num2)
    elif choice=="4":
        answer =div(num1,num2)
    else:
        print("Invalid choice")
        calculator()
    if answer:
        print("the result is",answer)
    while True:
        print("choose\n 1.continue\n2.exit")
        cont=int(input("enter: "))
        if cont == 1:
            calculator()
        else:
            print("exit")
            exit()
        

    

calculator()