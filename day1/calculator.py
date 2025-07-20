def pureAdd(*args):
  return sum(args)
def addition(a,b):
  return a+b

def subtraction(a,b):
  return a-b

def multiplication(a,b):
  return a*b

def division(a,b):
  return a/b

def floordivision(a,b):
  return a//b

def reminder(a,b):
  return a%b

def power(a,b):
  return a**b

def evalExpression(exp):
  return eval(exp)

def calculator():
  try:
    print('''List of expressions\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Floor division\n6)Power\n7)Evaluate an Expression\n\n\nEnter your choice : ''')
    choice = int(input())
    if 1<=choice<=8:
      if(choice<7):
        print("Enter 2 numbers to proceed with execution in the below format\n num1 num2")
        a,b=map(int,input().split())
      if choice == 1:
        return f"{a} + {b} = {addition(a,b)}"
      elif choice == 2:
        return f"{a} - {b} = {subtraction(a,b)}"
      elif choice == 3:
        return f"{a} * {b} = {multiplication(a,b)}"
      elif choice == 4:
        return f"{a} / {b} = {division(a,b)}"
      elif choice == 5:
        return f"{a} // {b} = {floordivision(a,b)}"
      elif choice == 6:
        return f"{a} ** {b} = {power(a,b)}"
      elif choice == 7:
        exp = input("Enter the expression to be executed :\n")
        return exp + " = " +str(evalExpression(exp))
    else:
      print("Invalid choice please enter a choice from given choices")
  except Exception as e:
    print(f"Invalid input: {e}")


def main():
  try:
    print(calculator())
    while True:
      print("\n1)Proceed for new calculations\n2)end\n")
      choice = int(input("Enter your choice : "))
      if choice == 1:
        print(calculator())
      else:
        print("thank you")
        break
  except Exception as e:
    print(f"Invalid input: {e}")
 

if __name__ == "__main__":
  main()


# print(pureAdd(*list(map(int,input().split()))))

# try:
#     print("Result:", eval(input("Enter your expression to evaluate: ")))
# except Exception as e:
#     print("Invalid expression:", e)


