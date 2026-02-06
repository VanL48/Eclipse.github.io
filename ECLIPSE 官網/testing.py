def load_record():
    global record
    with open("file.txt", "r") as f:
        record = [line.strip().split(";") for line in f.readlines()]

def print_record():
    for entry in record:
        print("\t".join(entry))

def search_tel_num(tel_num):
    for i, entry in enumerate(record):
        if entry[2] == tel_num:
            return i
    return -1

def delete_recordbytel_num(tel_num):
    row = search_tel_num(tel_num)
    if row != -1:
        for j in range(len(record[row])):
            record[row][j] = "---"
        print("The record is deleted.")

def add_record(firstname, lastname, tel_num, date, s_time, ppl):
    global record
    record.append([firstname, lastname, tel_num, date, s_time, ppl])

def update_file():
    with open("file.txt", "w") as f:
        for i, entry in enumerate(record):
            f.write(";".join(entry))
            if i < len(record) - 1:
                f.write("\n")

def day_table():
    global table
    with open("restaurant.txt", "r") as f:
        table = [line.strip().split(";") for line in f.readlines()]

def see_table():
    with open("restaurant.txt", "r") as f:
        for line in f:
            components = line.strip().split(';')
            date, time = components[0], components[1]
            integers = components[2:]

            count_0 = integers.count('0')
            count_2 = integers.count('2')
            count_4 = integers.count('4')
            print(f"Date: {date} Time: {time}")
            print(f"Occupied Table: {count_0}, Available amount of 2 seats table: {count_2}, Available amount of 4 seats table: {count_4}")

def search_table():
    pass  

def update_table(firstname, lastname, tel_num, date, s_time, ppl):  #AI
    with open("restaurant.txt", "r") as f:
        table_data = [line.strip().split(";") for line in f.readlines()]

    for i, entry in enumerate(table_data):
        if entry[0] == date and entry[1] == s_time:
            if int(ppl) <= 2:
                for j in range(2, len(entry)):  
                    if entry[j] == '2':
                        entry[j] = '0'  
                        break
            elif int(ppl) <= 4:
                for j in range(2, len(entry)):
                    if entry[j] == '4':
                        entry[j] = '0' 
                        break
            else:
                print("No suitable table available for the number of people.")
                return

            table_data[i] = entry
            
            with open("restaurant.txt", "w") as f:
                for line in table_data:
                    f.write(";".join(line) + "\n")
            print(f"Table updated for {firstname} {lastname} at {date} {s_time}.")
            return
            
    print("No matching reservation time found.") #AI
    
def delete_recordbytel_num(tel_num):
    row = search_tel_num(tel_num)
    if row != -1:
        firstname, lastname, tel_num, date, s_time, ppl = record[row]
        
        for j in range(len(record[row])):
            record[row][j] = "---"
        print("The record is deleted.")
        
        update_table_on_cancel(date, s_time, ppl)
    else:
        print("No record found to delete.")

def update_table_on_cancel(date, s_time, ppl): #AI
    with open("restaurant.txt", "r") as f:
        table_data = [line.strip().split(";") for line in f.readlines()]

    for i, entry in enumerate(table_data):
        if entry[0] == date and entry[1] == s_time:
            if int(ppl) <= 2:
                for j in range(2, len(entry)):
                    if entry[j] == '0':
                        entry[j] = '2'  
                        break
            elif int(ppl) <= 4:
                for j in range(2, len(entry)):
                    if entry[j] == '0':
                        entry[j] = '4'  
                        break
            else:
                print("No suitable table found to free.")
                return

            table_data[i] = entry
            
            with open("restaurant.txt", "w") as f:
                for line in table_data:
                    f.write(";".join(line) + "\n")
            print(f"Table updated back to available for {date} {s_time}.")
            return
            
    print("No matching reservation time found in the table data.") #AI

record = []
table = []

user = input("Select your action: \n -1 Exit \n 1: Print Record \n 2: Search Record \n 3: Delete Reservation \n 4: Do Reservation \n 5: Update the record \n 6: Check the current available seats ")
load_record()
day_table()

while user != "-1":
    if user == "1":
        print_record()
    elif user == "2":
        tel_num = input("Enter your phone number: ")
        found = search_tel_num(tel_num)
        if found != -1:
            print(record[found])
        else:
            print("Record not found.")
    elif user == "3":
        tel_num = input("Enter your phone number: ")
        delete_recordbytel_num(tel_num)
    elif user == "4":
        firstname = input("Enter a firstname: ")
        lastname = input("Enter a lastname: ")
        tel_num = input("Enter your phone number: ")
        date = input("Enter a reservation date: ")
        s_time = input("Enter your start time of reservation: ")   
        ppl = input("How many people? ")
        add_record(firstname, lastname, tel_num, date, s_time, ppl)        
        update_table(firstname, lastname, tel_num, date, s_time, ppl)  
        print("The record is added successfully.")
    elif user == "5":
        update_file()
        print("The record is updated successfully.")
    elif user == "6":
        see_table()
    
    user = input("Select your action: ")