import random
def main():
    print("Welcome to Zomato Chronicles: The Great Food Fiasco!")

    # Step 2: Menu Mastery
    menu = {
        1: {
            "name": "Pizza",
            "price": 12.99,
            "availability": True
        },
        2: {
            "name": "Burger",
            "price": 8.99,
            "availability": False
        },
        # Add more dishes to the menu.
    }
    count = 2
    orders = []

    while(True):
        print("Menu:")
        for dish_id, dish_info in menu.items():
            print(f"{dish_id}. {dish_info['name']} - ${dish_info['price']:.2f} ({'Available' if dish_info['availability'] else 'Not Available'})")

        print("Choices :")
        print("1. Add a new dish")
        print("2. Remove a dish")
        print("3. Update dish availability")
        print("4. Take a new Order")
        print("5. Review All order")
        print("6. Update the status of an order")
        print("7. filter all order by using status")
        print("8. Exit")


        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            count += 1
            dish_id = count
            name = input("Enter the dish name: ")
            price = float(input("Enter the dish price: "))
            availability = input("Is the dish available? (yes/no): ").lower() == 'yes'

            menu[dish_id] = {
                "name": name,
                "price": price,
                "availability": availability
            }

        elif choice == '2':
            dish_id = int(input("Enter the dish ID to remove: "))
            if dish_id in menu:
                del menu[dish_id]
                print("Dish removed successfully!")
            else:
                print("Invalid dish ID. The dish does not exist in the menu.")

        elif choice == '3':
            dish_id = int(input("Enter the dish ID to update availability: "))
            if dish_id in menu:
                availability = input("Is the dish available now? (yes/no): ").lower() == 'yes'
                menu[dish_id]['availability'] = availability
                print("Dish availability updated successfully!")
            else:
                print("Invalid dish ID. The dish does not exist in the menu.")

        elif choice == '4':
            # Exercise 6: Take a new order from a customer
            customer_name = input("Enter the customer's name: ")
            order_dish_ids = [int(x) for x in input("Enter dish IDs (comma-separated) the customer wants to order: ").split(',')]
            
            # Check if all dishes in the order are available
            order_available = all(menu[dish_id]['availability'] for dish_id in order_dish_ids)

            if order_available:
                # Process the order and assign a unique order ID
                order_id = generate_unique_order_id()
                print(f"Order for {customer_name} received. Order ID: {order_id}")

                # Update the order status as 'received'
                # You can decide on the data structure for storing orders, such as a list of dictionaries.
                # For now, let's assume we have an 'orders' list.
                orders.append({
                    "order_id": order_id,
                    "customer_name": customer_name,
                    "dish_ids": order_dish_ids,
                    "status": "recieved"
                })
            else:
                print("Sorry, some dishes in the order are not available. Cannot process the order.")
        elif choice == '5':
            if not orders:
                print("No orders yet. The kitchen is waiting for the first culinary adventure!")
            else:
                print("All Orders:")
                for order in orders:
                    print(f"Order ID: {order['order_id']}")
                    print(f"Customer Name: {order['customer_name']}")
                    print(f"Dish IDs: {', '.join(str(dish_id) for dish_id in order['dish_ids'])}")
                    print(f"Status: {order['status']}")
                    print()

        elif choice == '6':
            order_id_to_update = int(input("Enter the order ID to update status: "))

            # Find the order in the 'orders' list based on the order ID
            order_found = False
            for order in orders:
                if order['order_id'] == order_id_to_update:
                    order_found = True
                    new_status = input("Enter the new status (preparing/ready for pickup/delivered): ").lower()
                    order['status'] = new_status
                    print(f"Order ID {order_id_to_update} status updated to '{new_status}'.")
                    break

            if not order_found:
                print("Invalid order ID. The order does not exist.")
        elif choice == '7':
            print("You can filter All Orders")
            for_filter = input("Enter the new status (preparing/ready for pickup/delivered): ").lower()
            for order in orders:
                if order['status'] == for_filter:
                    print(f"Order ID: {order['order_id']}")
                    print(f"Customer Name: {order['customer_name']}")
                    print(f"Dish IDs: {', '.join(str(dish_id) for dish_id in order['dish_ids'])}")
                    print(f"Status: {order['status']}")
                    print()
        elif choice == '8':
            print("Exiting the program. Goodbye!")
            break
        # ... (previous code)

def generate_unique_order_id():
    return random.randint(1000, 9999)
if __name__ == "__main__":
    main()
