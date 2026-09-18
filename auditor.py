inventory = 0
failure_count = 0

while True:
    if inventory > 500:
        print("[ALERT] Inventory exceeded 500 units")
        break

    user_input_str = input("Enter stock quantity to add (e.g. 1, 67): ")

    if user_input_str == "quit":
        print("Quitting...")
        print("Total Units Processed:", inventory)
        print("Number of Failed/Rejected Entries:", failure_count)
        break

    if user_input_str.isdigit():
        user_input_int = int(user_input_str)
        inventory += user_input_int
    else:
        failure_count += 1
        print("[Error] User input is not a positive integer.")
