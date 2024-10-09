import struct, os
"""
[name, category, quantity_purchased, lasted_purchase_price, lasted_date, amount_used]
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
                lasted_date = int(input("Last Purchase Date (DD/MM/YYYY): "))
                amount_used = float(input("Amount: "))

                if len(name.strip()) == 0:
                    print("Error: Name cannot be empty.")
                    return

                data = struct.pack("20s20sffif", category.encode(), name.encode(), quantity_purchase, lasted_purchase_price, lasted_date, amount_used)
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
                lasted_date = int(input("Last Purchase Date (DD/MM/YYYY): "))
                amount_used = float(input("Amount: "))
                
                data = struct.pack("20s20sffif", category.encode(), name.encode(), quantity_purchase, lasted_purchase_price, lasted_date, amount_used)
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
    if not os.path.exists(file):
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

    print("Editing record:")
    name = input(f"New Name (current: {record_to_edit[1].decode().strip()}): ").ljust(20)[:20] or record_to_edit[1].decode().strip()
    category = input(f"New Category (current: {record_to_edit[0].decode().strip()}): ").ljust(20)[:20] or record_to_edit[0].decode().strip()
    
    try:
        quantity_purchase = float(input(f"New Quantity Purchased (current: {record_to_edit[2]:.2f}): ") or record_to_edit[2])
        lasted_purchase_price = float(input(f"New Last Purchase Price (current: {record_to_edit[3]:.2f}): ") or record_to_edit[3])
        lasted_date = int(input(f"New Last Purchase Date (current: {record_to_edit[4]}): ") or record_to_edit[4])
        amount_used = float(input(f"New Amount Used (current: {record_to_edit[5]:.2f}): ") or record_to_edit[5])
    except ValueError as e:
        print(f"Error: Invalid input. {e}")
        return

    updated_record = struct.pack("20s20sffif", category.encode(), name.encode(), quantity_purchase, lasted_purchase_price, lasted_date, amount_used)
    records[index] = struct.unpack("20s20sffif", updated_record)

    with open(file, "wb") as file_obj:
        for record in records:
            file_obj.write(struct.pack("20s20sffif", *record))

    print("Record updated successfully.")


#Read
def read_records(file) -> str:
    if not os.path.exists(file):
        print("Error: File Not Found!")
        return

    with open(file, "rb") as f:
        print("Result: ")
        print('_____________________________________________________________________________________________________________________________')
        print(f"{'Category':<20}{'Name':<20}{'Quantity(kg)':<20}{'Purchase Price(฿/k.g.)':<25}{'Last Purchase Date':<25}{'Amount Used(k.g.)':<10}")
        print('_____________________________________________________________________________________________________________________________')

        record_format = "20s20sffif"
        record_size = struct.calcsize(record_format)

        while True:
            record = f.read(record_size)
            if not record:
                break

            record = struct.unpack("20s20sffif", record)
            record = record[0].decode(), record[1].decode(), record[2], record[3], record[4], record[5]
            print(f"{record[0]}{record[1]:<24}{record[2]:<24.2f}{record[3]:<23.2f}{record[4]:<24}{record[5]:.2f}")


#Report
def report(file):
    if not os.path.exists(file):
        print("Error: File Not Found!")
        return

    record_format = "20s20sffif"
    record_size = struct.calcsize(record_format)

    total_values = {}

    with open(file, "rb") as f:
        while True:
            record = f.read(record_size)
            if not record:
                break
            category, name, quantity_purchased, lasted_purchase_price, lasted_date, amount_used = struct.unpack(record_format, record)

            category = category.decode().strip()
            name = name.decode().strip()
            remaining_quantity = quantity_purchased - amount_used
            value_of_remaining = remaining_quantity * lasted_purchase_price
            
            if category not in total_values:
                total_values[category] = {'items': [], 'total_value': 0.0}
            total_values[category]['items'].append({
                'name': name,
                'remaining_quantity': remaining_quantity,
                'value_of_remaining': value_of_remaining
            })
            total_values[category]['total_value'] += value_of_remaining

    print("\nInventory Report")
    print('___________________________________________________________________________________________________')
    print(f"{'Category':<20}{'Name':<20}{'Remaining Quantity (k.g.)':<35}{'Value of Remaining (฿)'}")
    print('___________________________________________________________________________________________________')

    for category, data in total_values.items():
        for item in data['items']:
            print(f"{category:<20}{item['name']:<29}{item['remaining_quantity']:<35.2f}{item['value_of_remaining']:.2f}")

        print(f"\nTotal value of remaining items in {category}: {data['total_value']:.2f} ฿")
        print('___________________________________________________________________________________________________')



#Find
def find_records(file) -> str:
    try:
        if not os.path.exists(file):
            raise FileNotFoundError("Error: File Not Found!")
        
        find = input("Which record are you looking for? (name, category, quantity_purchased, lasted_purchase_price, lasted_date, amount_used): ").lower()
        print("Result: ")
        v_record = {}
        count = 1
        found_records = 0

        print('_____________________________________________________________________________________________________________________________')
        print(f"{'Category':<20}{'Name':<20}{'Quantity(kg)':<20}{'Purchase Price(฿/kg)':<25}{'Last Purchase Date':<25}{'Amount Used(kg)':<10}")
        print('_____________________________________________________________________________________________________________________________')    

        with open(file, "rb") as f:
            record_format = "20s20sffif"
            record_size = struct.calcsize(record_format)

            while True:
                record = f.read(record_size)
                if not record:
                    break

                try:
                    unpacked = struct.unpack(record_format, record)
                except struct.error as e:
                    raise ValueError(f"Data unpacking error: {e}")

                record = struct.unpack("20s20sffif", record)
                record = record[0].decode(), record[1].decode(), record[2], record[3], record[4], record[5]

                v_record[count] = (
                    f"{record[0]}{record[1]:<24}{record[2]:<24.2f}{record[3]:<26.2f}{record[4]:<21}{record[5]:.2f}"
                )
                count += 1

        for key, value in v_record.items():
            if find in value.lower():
                print(value.upper())
                found_records += 1

        if found_records == 0:
            print(f"Not found: [{find}] in any records")
        print()

    except FileNotFoundError as fnf_error:
        print(fnf_error)

    except ValueError as ve:
        print(f"ValueError: {ve}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

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
