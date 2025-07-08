import csv
import json

def write_csv(filename):
    headers = input("Enter column headers (comma-separated): ").split(",")
    rows = []
    while True:
        row = input(f"Enter row data for {headers} (comma-separated) or 'done' to finish: ")
        if row.lower() == "done":
            break
        rows.append(row.split(","))

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"CSV file '{filename}' written successfully.")

def read_csv(filename):
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("File not found.")

def write_json(filename):
    json_data = {}
    key = input("Enter top-level key (e.g., 'employees'): ")
    json_data[key] = []
    while True:
        item = {}
        fields = input("Enter key=value pairs (comma-separated) or 'done' to finish: ")
        if fields.lower() == "done":
            break
        for field in fields.split(","):
            k, v = field.split("=")
            item[k.strip()] = v.strip()
        json_data[key].append(item)

    with open(filename, "w") as f:
        json.dump(json_data, f, indent=2)
    print(f"JSON file '{filename}' written successfully.")

def read_json(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            print(json.dumps(data, indent=2))
    except FileNotFoundError:
        print("File not found.")

def main():
    while True:
        print("\n--- CSV/JSON Read/Write Parser ---")
        print("1. Read CSV")
        print("2. Write CSV")
        print("3. Read JSON")
        print("4. Write JSON")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            read_csv(input("Enter CSV filename to read: "))
        elif choice == "2":
            write_csv(input("Enter CSV filename to write: "))
        elif choice == "3":
            read_json(input("Enter JSON filename to read: "))
        elif choice == "4":
            write_json(input("Enter JSON filename to write: "))
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
