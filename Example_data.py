import struct, os
"""
[name, category, quantity_purchased, lasted_purchase_price, lasted_date, price]
"""

#Create
def create_records(file):

    with open(file, "wb") as file_obj:
        try:
            count = int(input("How many records do you want to create?: "))  
        except ValueError as e:
            print(f"Error: Please enter a valid number. {e}")
            return  
        except Exception as e:
            print(f"Unexpected Error: {e}")
            return

        for i in range(count):
            try:

                print(f"\nRecord #{i + 1}:")
                name = input("Name: ").ljust(20)[:20]
                category = input("Category: ").ljust(20)[:20]  
                quantity_purchase = float(input("Quantity Purchased: "))
                lasted_purchase_price = float(input("Last Purchase Price: "))
                lasted_date = int(input("Last Purchase Date (YYYYMMDD): "))
                price = float(input("Price: "))

                if len(name.strip()) == 0:
                    print("Error: Name cannot be empty.")
                    return

                data = struct.pack("20s20sffif", category.encode(), name.encode(), quantity_purchase, lasted_purchase_price, lasted_date, price)
                file_obj.write(data)  
            except ValueError as e:
                print(f"Error: Invalid input. {e}")  
                return
            except Exception as e:
                print(f"Unexpected Error: {e}")
                return

        print(f"\nSuccessfully created {count} record(s)!")

#Add
def add_records(file):
    if not os.path.exists(file):
        print("Error: File Not Found!")
        return  

    with open(file, "ab") as file_obj:
        try:
            count = int(input("How many records to add?: ")) 
        except ValueError as e:
            print(f"Error: {e}")
            return  
        except Exception as e:
            print(f"Unexpected Error: {e}")
            return  

        for i in range(count):
            try:
                print(f"Record #{i + 1}:")
                name = input("Name: ").ljust(20)[:20]
                category = input("Category: ").ljust(20)[:20]  
                quantity_purchase = float(input("Quantity Purchased: "))
                lasted_purchase_price = float(input("Last Purchase Price: "))
                lasted_date = int(input("Last Purchase Date (YYYYMMDD): "))
                price = float(input("Price: "))
                
                data = struct.pack("20s20sffif", category.encode(), name.encode(), quantity_purchase, lasted_purchase_price, lasted_date, price)
                file_obj.write(data)  
            except ValueError as e:
                print(f"Error: {e}")
                return  
            except Exception as e:
                print(f"Unexpected Error: {e}")
                return  

        print(f"Successfully added {count} record(s)!")

#Edit
def edit_record(file):
    check = os.path.exists(file)
    if not check:
        print("Error: File Not Found!")
        return

    records = []  
    record_size = struct.calcsize("20s20sffif")  

    with open(file, "rb") as file_obj:
        while True:
            record = file_obj.read(record_size)
            if not record:
                break
            records.append(struct.unpack("20s20sffif", record))

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
    new_quantity_purchase = float(input(f"New Quantity Purchased (current: {record_to_edit[2]}): "))
    new_lasted_purchase_price = float(input(f"New Lasted Purchase Price (current: {record_to_edit[3]}): "))
    new_lasted_date = int(input(f"New Lasted Date (current: {record_to_edit[4]}): "))
    new_price = float(input(f"New Price (current: {record_to_edit[5]}): "))

    new_name = new_name if new_name.strip() else name.ljust(20)[:20]
    new_category = new_category if new_category.strip() else category.ljust(20)[:20]
    new_quantity_purchase = (new_quantity_purchase) if new_quantity_purchase else record_to_edit[2]
    new_lasted_purchase_price = (new_lasted_purchase_price) if new_lasted_purchase_price else record_to_edit[3]
    new_lasted_date = new_lasted_date if new_lasted_date else record_to_edit[4]
    new_price = new_price if new_price else record_to_edit[5]

    records[index] = (
        new_category.encode(),
        new_name.encode(),
        new_quantity_purchase,
        new_lasted_purchase_price,
        new_lasted_date,
        new_price)

    with open(file, "wb") as file_obj:
        for record in records:
            file_obj.write(struct.pack("20s20sffif", *record))

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
                      record = file.read(struct.calcsize("20s20sffif"))
                      if not record:
                            break
                      else:
                            record = struct.unpack("20s20sffif", record)
                            record = record[0].decode(), record[1].decode(), record[2], record[3], record[4], record[5]
                            print(f"=========================\n Name:{record[1]}\n Category:{record[0]}\n Quantity Purchased:{record[2]:.1f}kg.\n Lasted Purchase Price:{record[3]}\n Lasted Date:{record[4]}\n Price:{record[5]}฿\n=========================")
                print()

#Find
def find_records(file) ->str:
    check = os.path.exists(file)
    if check != True:
        print("Error: File Not File!")
    else:
        find = input("Which record are you looking for? (name, category, quantity_purchased, lasted_purchase_price, lasted_date, price): ")
        print("Result: ")
        v_record = {}
        count = 1
        vv = 0        

        with open(file, "rb") as file:
                while True:
                      record = file.read(struct.calcsize("20s20sffif"))
                      if not record:
                            break
                      else:
                        record = struct.unpack("20s20sffif", record)
                        record = record[0].decode(), record[1].decode(), record[2], record[3], record[4], record[5]
                        v_record[count] = (f"=========================\n Name:{record[0]}\n Category:{record[1]}\n Quantity Purchased:{record[2]:.1f}kg.\n Lasted Purchase Price:{record[3]}\n Lasted Date:{record[4]}\n Price:{record[5]}$\n=========================")
                        count += 1

                for key, value in v_record.items():
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
    record_size = struct.calcsize("20s20sffif")  

    with open(file, "rb") as file_obj:
        while True:
            record = file_obj.read(record_size)
            if not record:
                break
            records.append(struct.unpack("20s20sffif", record))

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
            file_obj.write(struct.pack("20s20sffif", *record))

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
