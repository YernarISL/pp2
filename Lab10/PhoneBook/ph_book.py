import psycopg2
import csv

conn = psycopg2.connect(
    host='localhost',
    dbname='PhoneBook',
    user='postgres',
    password='Ernar03092005'
)

cur = conn.cursor()

cur.execute('DROP TABLE book')
conn.commit()

cur.execute(
    """
    CREATE TABLE book (
    ID INT PRIMARY KEY,
    Name VARCHAR(20),
    Number VARCHAR(20),
    Age INT,
    Mail VARCHAR(50),
    City VARCHAR(255),
    Profession VARCHAR(30)
    )
    """
)

def outputData(result):
    for every in result:
        print(every)

class PhoneBook():
    def __init__(self):
        self.csv_input = False
        self.console_input = False
        self.upload_more = False
        self.update_status = False
        self.select_status = False
        self.delete_status = False

    def insertion(self):
        self.choice = input("1. Upload Data from CSV \n2. Upload data from console\n")
        if self.choice == '1':
            self.csv_input = True
        elif self.choice == '2':
            self.console_input = True
        else:
            print("Incorrect data")

    def consoleUpload(self):
        self.id = int(input("ID: "))
        self.name = input("Name: ")
        self.number = input("Number: ")
        self.age = int(input("Age: "))
        self.mail = input("Mail: ")
        self.city = input("City: ")
        self.prof = input("Profession: ")
        
        cur.execute(
            f"""
            INSERT INTO book (ID, Name, Number, Age, Mail, City, Profession) VALUES
            ({self.id}, '{self.name}', '{self.number}', {self.age}, '{self.mail}', '{self.city}', '{self.prof}')
            """
        )
        conn.commit()

        self.upload = input("Upload more? \n1. YES \n2. NO\n")
        if self.upload == '1':
            self.upload_more = True
        elif self.upload == '2':
            self.upload_more = False
        else:
            print("Incorrect data")

    def update(self):
        self.upd = input("Update data? \n1. YES \n2. NO\n")

        if self.upd == '1':
            self.option = input("Select Change:\n1. Name \n2. Phone number\n")
            if self.option == '1':
                self.update_status = True
                self.condition = int(input("ID: "))
                self.updated_name = input("Updated name: ")
                cur.execute(f"""UPDATE book SET Name = '{self.updated_name}' WHERE ID = {self.condition}""")        
                conn.commit()
            elif self.option == '2':
                self.update_status = True
                self.updated_number = input("Updated number: ")
                cur.execute(f"""UPDATE book SET Number = '{self.updated_number}' WHERE ID = {self.condition}""")
                conn.commit()
        elif self.upd == '2':
            self.update_status = False
        else:
            print("Incorrect data")

    def selection(self):
        self.select_needed = input("Select data? \n1. YES \n2. NO\n")
        if self.select_needed == '1':
            self.select_status = True
            self.option = input("Select by: \n1. City \n2. Age \n")
            if self.option == '1':
                city = input("City: ")
                cur.execute(f"""SELECT * FROM book WHERE City = '{city}'""")
                result = cur.fetchall()
                for every in result:
                    print(every)
            elif self.option == '2':
                cur.execute(f"""SELECT * FROM book ORDER BY Age""")
                result = cur.fetchall()
                for every in result:
                    print(every)
        elif self.select_needed == '2':
            self.select_status = False
        else:
            print("incorrect data")

    def deleting(self):
        self.delete_needed = input("Delete data? \n1.YES \n2.NO\n")
        if self.delete_needed == '1':
            self.delete_status = True
            self.option = input("Delete by: \n1. Name \n2. Phone \n")
            if self.option == '1':
                name = input("Name: ")
                cur.execute(f"""DELETE FROM book WHERE Name = '{name}'""")
                conn.commit()
                
            elif self.option == '2':
                self.delete_status = False
            else:
                print("Incorrect data")
            
contact = PhoneBook()
contact.insertion()

# CSV
if contact.csv_input:
    filename = 'data2.csv'

    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        for row in csvreader:
            idn, name, num, age, mail, city, prof = row
            cur.execute(f"""INSERT INTO book (ID, Name, Number, Age, Mail, City, Profession) VALUES
                        ({idn}, '{name}', '{num}', {age}, '{mail}', '{city}', '{prof}')""")
            conn.commit()

    conn.commit()
    contact.update()
    while contact.update_status:
        contact.update()
    contact.selection()
    while contact.select_status:
        contact.selection()
    contact.deleting()
    while contact.delete_status:
        contact.deleting()

# Console
elif contact.console_input:
    contact.consoleUpload()
    while contact.upload_more:
        contact.consoleUpload()
    contact.update()
    while contact.update_status:
        contact.update()
    contact.selection()
    while contact.select_status:
        contact.selection()
    contact.deleting()
    while contact.delete_status:
        contact.deleting()