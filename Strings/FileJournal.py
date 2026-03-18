FileName = 'journal.txt'

def write_entry():
    entry = input("Write your journal entry: ")
    with open(FileName, 'a') as file:
        file.write(entry + "\n")   # add newline for readability

def read_all():
    with open(FileName, 'r') as file:
        print("\nAll Journal Entries:")
        print(file.read())

def search():
    keyword = input("Enter a keyword to search: ")
    with open(FileName, 'r') as file:
        all_lines = file.readlines()
        for line in all_lines:
            if keyword.lower() in line.lower():
                print(line.strip())
                return
    print("No Matching Entries")

def main_menu():
    while True:
        print('\n >>>>> File Journal Menu <<<<<')
        print('1. Add Entry')
        print('2. Read All Entries')
        print('3. Search Entries')
        print('4. Exit')
        choice = int(input("Enter choice from 1 to 4: "))
        if choice == 1:
            write_entry()
        elif choice == 2:
            read_all()
        elif choice == 3:
            search()
        elif choice == 4:
            print("Thanks")
            break
        else:
            print("Invalid Option")

if __name__ == "__main__":
    main_menu()

    





