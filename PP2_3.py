

def q1(): 
  word = input("In: ")
  if word[-1] == "y":
    print("-ies")
  elif word[-1] == "ey":
    print("-eys")
  elif word[-1] == "ife":
    print("-ives")
  else:
    print("-s")


def q2(): 
  num = int(input("In: "))
  if num > 0:
    print(f"{num} is positive")
  elif num < 0:
    print(f"{num} is negative")
  
def q3():
  num1 = float(input("Input a number: "))
  num2 = float(input("Input a number: "))
  num3 = float(input("Input a number: "))
  if num1 != num2 and num1 != num3 and num2 != num3:
    print("Scalene")
  elif num1 == num2 and num1 != num3 or num1 == num3 and num1 != num2:
    print("Isosceles")
  elif num1 == num2 and num1 == num3:
    print("Equilateral")
  elif num1 + num2 < num3 or num1 + num3 < num2 or num2 + num3 < num1:
    print("No Triangle")





#Do not alter the following code
#Comment out the following code when running your tests
'''
q1()
q2()
'''

