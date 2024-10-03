import struct, os
"""
[name, category, quantity_purchase, lasted_purchase_price, lasted_date, price]
"""

#Create
def create_records(file):

    with open(file, "wb") as file:
        count = 0
        try:
              count = int(input("How record to create?: "))
        except ValueError as e:
              print(f"Error: {e}")
        except Exception as e:
              print(f"Error: {e}")
        else:
                for i in range(count):
                        try:
                                print(f"Number #{count +1}")
                                name = input("Name: ")
                                category = input("Category: ")
                                quantity_purchase = float(input("Quantity_purchase: "))
                                lasted_purchase_price = input()
                                lasted_date = input()
                                price = input()

                        except ValueError as e:
                                print(f"Error: {e}")
                                break
                        except Exception as e:
                                print(f"Error: {e}")
                                break

                        else:
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
