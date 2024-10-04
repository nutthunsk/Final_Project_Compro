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
    if not check:
        print("Error: File Not Found!")
        return

    records = []  
    record_size = struct.calcsize("i20si20sf")  

    with open(file, "rb") as file_obj:
        while True:
            record = file_obj.read(record_size)
            if not record:
                break
            records.append(struct.unpack("i20si20sf", record))

    print("Current Records:")
    for idx, record in enumerate(records):
        name = record[1].decode().strip()
        category = record[0].decode().strip()
        print(f"{idx + 1}: [Name: {name}, Category: {category}]")

    try:
        index = int(input("Enter the record number you want to edit: ")) - 1
        if index < 0 or index >= len(records):
            print("Error: Invalid record number.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        return

    record_to_edit = records[index]
    name = record_to_edit[1].decode().strip()
    category = record_to_edit[0].decode().strip()

    print(f"Editing record: [Name: {name}, Category: {category}]")

    new_name = input(f"New Name (leave blank to keep '{name}'): ").ljust(20)[:20]
    new_category = input(f"New Category (leave blank to keep '{category}'): ").ljust(20)[:20]
    new_quantity_purchase = input(f"New Quantity Purchase (current: {record_to_edit[2]}): ")
    new_lasted_purchase_price = input(f"New Lasted Purchase Price (current: {record_to_edit[3]}): ")
    new_lasted_date = input(f"New Lasted Date (current: {record_to_edit[4]}): ")
    new_price = input(f"New Price (current: {record_to_edit[5]}): ")

    new_name = new_name if new_name.strip() else name.ljust(20)[:20]
    new_category = new_category if new_category.strip() else category.ljust(20)[:20]
    new_quantity_purchase = float(new_quantity_purchase) if new_quantity_purchase else record_to_edit[2]
    new_lasted_purchase_price = float(new_lasted_purchase_price) if new_lasted_purchase_price else record_to_edit[3]
    new_lasted_date = int(new_lasted_date) if new_lasted_date else record_to_edit[4]
    new_price = float(new_price) if new_price else record_to_edit[5]

    records[index] = (
        new_category.encode(),
        new_name.encode(),
        new_quantity_purchase,
        new_lasted_purchase_price,
        new_lasted_date,
        new_price)

    with open(file, "wb") as file_obj:
        for record in records:
            file_obj.write(struct.pack("i20si20sf", *record))

    print("Record updated successfully.")

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
    check = os.path.exists(file)
    if check != True:
        print("Error: File Not File!")
    else:
        find = input("Which record are you looking for? (name, category, quantity_purchase, lasted_purchase_price, lasted_date, price)")
        print("Result: ")
        record = {}
        count = 1
        vv = 0        

        with open(file, "rb") as file:
                while True:
                      record = file.read(struct.calcsize("i20si20sf"))
                      if not record:
                            break
                      else:
                        record = struct.unpack("i20si20sf", record)
                        record = record[0].decode(), record[1].decode(), record[3], record[4], record[5]
                        record[count] = (f"[Name:{record[0]}, Category:{record[1]}, Quantity Purchase:{record[2]}, Lasted Purchase Price:{record[3]}, Lasted Date:{record[4]}, Price:{record[5]}$]")
                        count += 1

                for key, value in record.items():
                      if find in value:
                        print(value)
                        vv += 1
                      else:
                        continue
                if vv == 0:
                      print(f"Not found  [{find}] in any records")
                print()

#Remove
def remove_record(file):
    check = os.path.exists(file)
    if not check:
        print("Error: File Not Found!")
        return

    records = []  
    record_size = struct.calcsize("i20si20sf")  

    with open(file, "rb") as file_obj:
        while True:
            record = file_obj.read(record_size)
            if not record:
                break
            records.append(struct.unpack("i20si20sf", record))

    print("Current Records:")
    for idx, record in enumerate(records):
        name = record[1].decode().strip()
        category = record[0].decode().strip()
        print(f"{idx + 1}: [Name: {name}, Category: {category}]")

    try:
        index = int(input("Enter the record number you want to remove: ")) - 1
        if index < 0 or index >= len(records):
            print("Error: Invalid record number.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        return

    record_to_remove = records[index]
    name = record_to_remove[1].decode().strip()
    category = record_to_remove[0].decode().strip()

    confirm = input(f"Are you sure you want to remove the record [Name: {name}, Category: {category}]? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Record removal canceled.")
        return

    del records[index]

    with open(file, "wb") as file_obj:
        for record in records:
            file_obj.write(struct.pack("i20si20sf", *record))

    print("Record removed successfully.")

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
