inventory_count: int = 0
failure_count: int = 0
DOLLOR_COST_PER_ITEM: float = 1.0
TAX: float = 1.10


def get_valid_input():
    user_input_str = input("Enter stock quantity to add (e.g. 1, 67): ")
    if user_input_str == "quit":
        raise KeyboardInterrupt("User entered 'quit'.")
    if user_input_str.isdigit():
        return  int(user_input_str)
    else:
        raise ValueError("[Error] User input is not a positive integer.")


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * TAX


def generate_report(total_units, failed_attempts):
    print(f"Total Units Processed: {total_units}")
    print(f"Total cost(tax inclusive): {calculate_tax(total_units):0.2f}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


while True:
    if inventory_count > 500:
        print("[ALERT] Inventory exceeded 500 units")
        break
        
    try:
        user_input = get_valid_input()
    except KeyboardInterrupt:
        print("Quitting...")
        generate_report(inventory_count, failure_count)
        break
    except ValueError:
        failure_count += 1
        print("[Error] User input is not a positive integer.")
        break
    
    inventory_count = process_delivery(inventory_count, user_input)
