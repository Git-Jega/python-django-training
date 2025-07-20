import datetime

def log_exception(e):
    with open("day4/error_log.txt", "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {type(e).__name__}: {str(e)}\n")

def main():
    try:
        # Example risky code
        num = int(input("Enter a number: "))
        result = 10 / num
        print(f"Result is: {result}")
    except Exception as e:
        print("An error occurred. Check error_log.txt for details.")
        log_exception(e)

if __name__ == "__main__":
    main()
