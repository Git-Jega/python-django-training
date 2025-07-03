class contact_book:
  def __init__(self):
    self.contact_book = dict()
  
  def update_contact(self):
    name = input("Enter name: ")
    number = input("Enter number: ")
    if name not in self.contact_book.keys():
      print(f"There is no contact with name {name}")
    else:
      self.contact_book.update({name:number})
      print(f"Contact for {name} added/updated")

  def add_contact(self):
    name = input("Enter name: ")
    number = input("Enter number: ")
    self.contact_book.update({name:number})
    print(f"Contact for {name} added/updated")
  
  def delete_contact(self):
    name = input("Enter name: ")
    if name not in self.contact_book.keys():
      print(f"We couldn't delete it because contact with {name} is not available")
    else:
      self.contact_book.pop(name,None)
      print(f"Contact for {name} deleted")

  def retrieve_contact(self):
    name = input("Enter name: ")
    contact = self.contact_book.get(name)
    if contact:
      print(f"The contact number for {name} is {contact}")
    else:
      print(f"There is not contact record for {name}")

def main():
  print("""---------- Welcome to contact book ----------
          What you want to do
        1)Add a new contact
        2)Update an existing contact
        3)Retrieve an existing contact
        4)Delete an existing contact""")
  options = {
        1: book.add_contact,
        2: book.update_contact,
        3: book.retrieve_contact,
        4: book.delete_contact
  }
  try:
    choice = int(input("\nEnter your choice : "))
    action = options.get(choice)
    if action:
      action()
    else:
      print("Invalid Choice")
  except ValueError:
    print("please enter a valid input")
if __name__ == "__main__":
  book = contact_book()
  while True:
    main()
    try:
      c = int(input("\n1)Continue for any new action\n2)Exit\nEnter your choice : "))
      if c==2:
        break
    except ValueError:
      print("please enter a valid input")
