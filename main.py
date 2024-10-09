import Example_data as md

def Run():
    runing = True

    print("_______ Welcome! _______\n")
    file = input("File Path: ")
    print("_____________________________\n1.Create records\n2.Add records\n3.Edit record\n4.Show records\n5.Report record\n6.Find record\n7.Remove record\n8.Delete file record\n9.Exit\n_____________________________")
    while runing:
        choice = input("Action (1-9): ")

        if choice not in ["1", "2", "3", "4", "5", "6", "7","8","9"]:
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
                    md.report(file)
                case "6":
                    md.find_records(file)
                case "7":
                    md.remove_record(file)
                case "8":
                    md.delete_record(file)
                case "9":
                    print("Exiting program...")
                    break

if __name__ == "__main__":
    Run()
