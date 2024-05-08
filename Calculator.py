
def userChoice(number: int):
   if number == 1:
      x = float(input("enter the first number: "))
      y = float(input("enter the second number: "))
      Additions(x, y)
   elif number == 2:
      x=float(input("Enter the first number: "))
      y = float(input("enter the number you wish to substract from the first: "))
      Substraction(x,y)
   elif number == 3:
      x = float(input("Enter the first number: "))
      y = float(input("enter the number you wish to divide from the first: "))
      Division(x, y)
   elif number == 4:
      x = int(input("Enter the first number: "))
      y = int(input("Enter the second number: "))
      Remainder(x, y)
   elif number == 5:
      x=int(input("Enter the number for the multiplication table: "))
      y=int(input("Enter the limit : "))
      Multiplication(x, y)
   elif number == 6:
      print("You chose to quit, Thank you for using this program.")
   else:
      print("Wrong Input, sorry.")


def Additions(x:float, y:float):
   result = x+y
   print(str(x)+"+"+str(y)+"="+str(result))

def Substraction(x:float, y:float):
   result = x - y
   print(str(x) + "-" + str(y) + "=" + str(result))

def Division(x:float, y:float):
   result = x / y
   print(str(x) + "/" + str(y) + "=" + str(result))

def Remainder(x:float, y:float):
   result = x % y
   print(str(x) + "%" + str(y) + "=" + str(result))

def Multiplication(x:int, y:int):
   num = -1
   while num<y:
      num = num + 1
      print(str(num)+"*"+str(x)+"="+str(num*x))



number=0
while number!=6:
 print("-----------------")
 print("1- Make Additions")
 print("2- Make Substractions")
 print("3- Make Divisions")
 print("4- Get Remainder")
 print("5- See Tables of Multiplication")
 print("6- To Quit/Stop")
 print("-----------------")
 number = int(input("Enter your choice: "))
 userChoice(number)
