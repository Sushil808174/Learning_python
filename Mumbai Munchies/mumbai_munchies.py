
snack_inventory = [
    {
        "snack_id": 1,
        "name": "Potato Chips",
        "price": 20,
        "availability": True,  
    },
    {
        "snack_id": 2,
        "name": "Samosa",
        "price": 15,
        "availability": True,
    },
    # Add more snacks to the inventory if needed
]

# Initialize an empty list to store sales records
sales_records = []



def displayAllFunctionality():
    print("1. Display all inventory")
    print("2. Add snack in inventory")
    print("3. Update availability of a snack")
    print("4. Remove snack from inventory")
    print("5. Exit")

def addSnack(count):
    print("Add a New Snack to the Inventory:")
    snack_name = input("Enter Snack Name: ")
    snack_price = float(input("Enter Snack Price: "))
    availability = input("Is the Snack Available? (yes/no): ").lower() == "yes"
    # Create a dictionary to represent the new snack
    new_snack = {
        "snack_id": count,
        "name": snack_name,
        "price": snack_price,
        "availability": availability,
    }

    # Add the new snack to the inventory list
    snack_inventory.append(new_snack)

    print()
    print(f"Snack '{snack_name}' with ID {count} added to the inventory.")
    print()


def updateAvailability():
    snack_id_to_update = int(input("Enter the Snack ID to update availability: "))

    # Find the snack in the inventory based on the provided snack ID
    found_snack = None
    for snack in snack_inventory:
        if snack["snack_id"] == snack_id_to_update:
            found_snack = snack
            break

    if found_snack:
        new_availability = input("Is the Snack Available? (yes/no): ").lower() == "yes"
        found_snack["availability"] = new_availability
        print()
        print(f"Availability of snack '{found_snack['name']}' with ID {found_snack['snack_id']} updated.")
        print()
    else:
        print()
        print(f"Snack with ID {snack_id_to_update} not found in the inventory.")
        print()

def removeSnack():
    snack_id_to_remove = int(input("Enter the Snack ID to remove from the inventory: "))

    found_snack = None
    for snack in snack_inventory:
        if snack["snack_id"] == snack_id_to_remove:
            found_snack = snack
            break

    if found_snack:
        snack_inventory.remove(found_snack)
        print(f"Snack '{found_snack['name']}' with ID {found_snack['snack_id']} removed from the inventory.")
    else:
        print(f"Snack with ID {snack_id_to_remove} not found in the inventory.")


def display_inventory():
    print("Snack Details :")
    print()
    
    for snack in snack_inventory:
        print("Snack ID :",snack['snack_id'])
        print("Name :",snack['name'])
        print("Price :",snack['price'])
        print("Availability :",snack['availability'])
        print()

count = 2
while(True):
    displayAllFunctionality()
    choice = int(input("Enter Your Choice : "))
    
    if choice == 1:
        display_inventory()
    if choice == 2:
        count+=1
        addSnack(count)
    if choice == 3:
        updateAvailability()
    if choice == 4:
        removeSnack()
    if choice == 5:
        break

