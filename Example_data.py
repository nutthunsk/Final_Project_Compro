import struct, os
"""
[category, name, amount, data, balance, price]
"""

#Create
def create_records(file):

    with open(file, "wb") as file:
        pass

#Add
def add_records(file):

    with open(file, "ab") as file:
        pass

#Edit
def edit_record(file):
        check = os.path.exists(file)
        if check != True:
             print("Error: File Not Found!")
        pass

#Read
def read_records(file) ->str:

    with open(file, "rb") as file:
        pass

#Find
def find_records(file) ->str:

    with open(file, "rb") as file:
        pass

#Remove
def remove_record(file):
        check = os.path.exists(file)
        if check != True:
             print("Error: File Not Found!")
        pass

#Delete
def delete_record(file):
        check = os.path.exists(file)
        if check != True:
                print("Error: File Not Found!!")
        else:
                q = input("Confirm type (Yes,No): ")
                if q.lower() == "yes":
                        os.remove(file)
                        print(f"{file} Removed!!")
                else:
                        print("Removing has been Stoped!!")
