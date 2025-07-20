def action(choice, text=None):
    try:
        if choice == 1:
            with open("day4/demofile.txt", "r") as f:
                print("\nFile content:\n" + f.read())
        elif choice == 2:
            with open("day4/demofile.txt", "w") as f:
                f.write(text)
                print("File overwritten successfully.")
        elif choice == 3:
            with open("day4/demofile.txt", "a") as f:
                f.write(text)
                print("Text appended successfully.")
        else:
            print("Please choose a valid option.")
    except FileNotFoundError:
        print("Error: File not found. Make sure 'day4/demofile.txt' exists.")
    except PermissionError:
        print("Error: Permission denied. Check file permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    while True:
        try:
            print("\n\tFile Read/Write")
            print("1) Read a file")
            print("2) Write to a file")
            print("3) Append text to an existing file")
            print("4) Exit")
            choice = int(input("Please enter your choice: "))

            if choice == 4:
                print("Exiting program.")
                break
            elif choice in [2, 3]:
                text = input("Enter text to perform action: ")
                action(choice, text)
            elif choice == 1:
                action(choice)
            else:
                print("Invalid choice. Please select from 1 to 4.")
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
  main()