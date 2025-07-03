class Queue:
  def __init__(self):
    self.queue = []
  def size(self):
    return len(self.queue)
  def isEmpty(self):
    return True if self.size() == 0 else False
  def enqueue(self):
    element = input("Enter an element to add in queue : ")
    self.queue.append(element)
    return f"Successfully added {element} to queue"
  def dequeue(self):
    if self.size() == 0:
      return "There are no elements in the queue to perform this operation"
    self.queue.pop(0)
    return f"Successfully popped an element from queue"
  def peek(self):
    if self.size() == 0:
      return "There are no elements in the queue to perform this operation"
    return self.queue[0]
  
def main():
  print("""---------- Welcome to custom stack implementation using List ----------
          What you want to do
        1)Enqueue
        2)Dequeue
        3)peek
        4)size
        5)check if stack is empty""")
  options = {
    1 : cus_stack.enqueue,
    2 : cus_stack.dequeue,
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
  cus_stack = Queue()
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
