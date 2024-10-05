import Example_data as md

def Run():
    runing = True

    print("Welcome!\n")
    file = input("File Path: ")
    print("_____________")
    print("1.Create records\n2.Add records\n3.Edit record(unfinished)\n4.Show records\n5.Find record\n6.Remove record(unfinished)\n7.Delete file record")
    print("_____________")
    while runing:
        choice = input("Action (1-7): ")

        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Error: ValueError")
            runing = False
        else:
            match choice:
                case "1":
                    md.create_records(file)
                case "2":
                    md.add_records(file)
                case "3":
                    md.edit_record(file)
                case "4":
                    md.read_records(file)
                case"5":
                    md.find_records(file)
                case "6":
                    md.remove_record(file)
                case "7":
                    md.delete_record(file)

if __name__ == "__main__":
    Run()
