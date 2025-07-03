class stack:
  def __init__(self):
    self.stack = []
  def size(self):
    return len(self.stack)
  def isEmpty(self):
    return True if self.size() == 0 else False 
  def push(self):
    element = input("Enter an element to add in stack : ")
    self.stack.append(element)
    return "successfully pushed to the stack"
  def pop(self):
    if self.size()>0:
      self.stack.pop()
      return "successfully popped the stack"
    else:
      return "stack is empty to perform the action"
  def peek(self):
    if self.size()>0:
      return self.stack[-1]
    else:
      return "stack is empty to perform the action"
  
def main():
  print("""---------- Welcome to custom stack implementation using List ----------
          What you want to do
        1)push
        2)pop
        3)peek
        4)size
        5)check if stack is empty""")
  options = {
    1 : cus_stack.push,
    2 : cus_stack.pop,
    3 : cus_stack.peek,
    4 : cus_stack.size,
    5 : cus_stack.isEmpty
  }
  try:
    choice = int(input())
    action = options.get(choice)
    if action:
      print(action())
    else:
      print("Invalid choice")
  except ValueError:
    print("please enter a valid input")

if __name__ == "__main__":
  cus_stack = stack()
  while True:
    main()
    try:
      c = int(input("\n1)Continue for any new action\n2)Exit\nEnter your choice : "))
      if c==2:
        break
      elif c==1:
        continue
      else:
        print("Not an valid input")
        break  
    except ValueError:
      print("please enter a valid input")
