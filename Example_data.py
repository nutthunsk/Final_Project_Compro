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
                                quantity_purchase = float(input("Quantity Purchase: "))
                                lasted_purchase_price = float(input("Lasted Purchase Price: "))
                                lasted_date = int(input("Lasted Date: "))
                                price = float(input("Price: "))
                        except ValueError as e:
                                print(f"Error: {e}")
                                break
                        except Exception as e:
                                print(f"Error: {e}")
                                break
                        else:
                              data = struct.pack("i20si20sf", category.encode(), name.encode(), quantity_purchase, lasted_purchase_price,  lasted_date, price)
                              file.write(data)
                              count += 1
                              break

                print(f"Done! {count}")

#Add
def add_records(file):
    check = os.path.exists(file)
    if check != True:
          print("Error: File Not Found!")
    else:
          with open(file, "ab") as file:
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
                                quantity_purchase = float(input("Quantity Purchase: "))
                                lasted_purchase_price = float(input("Lasted Purchase Price: "))
                                lasted_date = int(input("Lasted Date: "))
                                price = float(input("Price: "))
                            except ValueError as e:
                                print(f"Error: {e}")
                            except Exception as e:
                                print(f"Error: {e}")
                            else:
                                data = struct.pack("i20si20sf", category.encode(), name.encode(), quantity_purchase, lasted_purchase_price,  lasted_date, price)
                                file.write(data)
                                count += 1
                                break 

                print(f"Done! {count}")
#Edit
def edit_record(file):
        check = os.path.exists(file)
        if check != True:
             print("Error: File Not Found!")
        pass

#Read
def read_records(file) ->str:
    check = os.path.exists(file)
    if check != True:
          print("Error: File Not Found!")

    else:
        with open(file, "rb") as file:
                print("Result: ")
                while True:
                      record = file.read(struct.calcsize("i20si20sf"))
                      if not record:
                            break
                      else:
                            record = struct.unpack("i20si20sf", record)
                            record = record[0].decode(), record[1].decode(), record[3], record[4], record[5]
                            print(f"[Name:{record[0]}, Category:{record[1]}, Quantity Purchase:{record[2]}, Lasted Purchase Price:{record[3]}, Lasted Date:{record[4]}, Price:{record[5]}$]")
                print()

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
