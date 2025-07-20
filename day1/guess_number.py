import random

def number_game():
  try:
    random_number = random.randint(1,100)
    print("\nYou should guess the number in 4 guesses \n\nNOTE: the number will be between 1 to 100 inclusive of edge values\n")
    i=1
    while i<5:
      n = int(input(f"Give your guess {i} : "))
      if random_number == n:
        print("Congratuations you win !!!")
        i += 1
      else:
        if i==4:
          print("\t\nYou Lose")
        i += 1
        continue
  except Exception as e:
    print(f"Invalid input: {e}")

def main():
  number_game()
  choice= int(input("\n1)Play again\n2)exit\n\n"))
  if choice == 1:
    number_game()
  else:
    print("Thank you")
if __name__ == "__main__":
  main()