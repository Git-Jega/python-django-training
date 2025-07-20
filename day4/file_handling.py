# "x" - Create - will create a file, returns an error if the file exists

# "a" - Append - will create a file if the specified file does not exists

# "w" - Write - will create a file if the specified file does not exists

import os
def main():
  a = open("day4/demofile.txt")
  print(a.read())
  a.close()
  with open("day4/demofile.txt","r") as f:
    # using 'with' keyword closes the file automatically after execution
    print(f.read())
  with open("day4/demofile.txt") as f:
    # we can specify how many characters we want to read
    print(f.read(5))
  with open("day4/demofile.txt") as f:
    # # readLine() can be used to read a line from the file we can call it 2 times to read the first two lines in the file
    print(f.readline())
    print(f.readline())
  with open("day4/demofile.txt") as f:
    # By looping through the lines of the file, we can read the whole file, line by line
    for i in f:
      print(i)
  with open("day4/demofile.txt","w") as f:
    f.write("hi")
  with open("day4/demofile.txt","w") as f:
    f.write("""Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!""")
  # with open("day4/demofile.txt","a") as f:
  #   f.writelines(["hi","jega"])
  # with open("day4/demofile.txt","a") as f:
  #   f.write("\nhi")
  # #create a new file
  # f = open("day4/demofiles.txt","x")
  # f.write("hi")
  # os.remove("day4/demofiles.txt")
  # os.mkdir("day4/fold")
  # os.rmdir("day4/fold")
if __name__ == "__main__":
  main()