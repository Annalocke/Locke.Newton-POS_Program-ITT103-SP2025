# Create a dictionary to store the store product details
products = {
    "Milk": [1500.00, 10], "Bread": [620.00, 15], "Eggs": [600.00, 8], "Rice": [1000.00, 5],
    "Chicken": [2000.00, 6], "Soap": [300.00, 10], "Shampoo": [900.00, 3], "Conditioner": [1000.00, 12],
    "Water": [150.00, 20], "Sugar": [700.00, 4]
}

cart = {}  # Create a dictionary to store items in the cart


def addCart():
    # Add items to the cart and Loop until a valid product name is entered
    while True:
        product_name = input("Enter product name: ")
        if product_name in products:
            break
        else:
            print("Product not found. Please enter a valid product name.")

    # Loop until a valid quantity is entered
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0 and quantity <= products[product_name][1]:
                break
            else:
                print("Invalid quantity or insufficient stock.")
        except ValueError:
            print("Invalid Input. Please enter a valid number for the quantity.")

    # Add the item to the cart and update stock
    cart[product_name] = cart.get(product_name, 0) + quantity
    products[product_name][1] -= quantity
    print(f"{quantity} {product_name} added to cart.")

    # Check for low stock (quantity remaining is less than 5) after an item is added to the cart
    if products[product_name][1] < 5:
        print(f"Low-Stock Alert: There are only {products[product_name][1]} {product_name} left in stock.")


def removeCart():
    # Check if the cart is empty before prompting the cachier/user to enter an item to be removed
    if not cart:
        print("Your cart is empty. There is nothing to be removed.")
        return

    # Removes an item from the cart
    product_name = input("Enter product name to remove: ")
    if product_name in cart:
        products[product_name][1] += cart[product_name]
        del cart[product_name]  # removing cart name from the dictionary
        print(f"{product_name} removed from cart.")
    else:
        print("Item not found in cart.")


def viewCart():
    total = 0
    print("\nShopping Cart:")
    for item, quantity in cart.items():
        price = products[item][0]
        total += price * quantity
        print(f"{item}: {quantity} x ${price} = ${price * quantity}")
    print(f"Total: ${total:.2f}")


def checkout():
    # Processes payment and generates a receipt
    if not cart:
        print("Cart is empty. Please add items before checking out.")
        return

    subtotal = sum(products[item][0] * quantity for item, quantity in cart.items())
    tax = subtotal * 0.10
    discount = 0.05 * subtotal if subtotal > 5000 else 0
    total = subtotal + tax - discount

    print(
        f"\nSubtotal: ${subtotal:.2f}\nSales Tax (10%): ${tax:.2f}\nDiscount:${discount:.2f}\nTotal Due: ${total:.2f}")

    while True:
        try:
            amount_paid = float(input("Enter amount paid: "))
            if amount_paid >= total:
                change = amount_paid - total
                print(f"Change: ${change:.2f}\n")
                generate_receipt(subtotal, tax, discount, total, amount_paid, change)
                cart.clear()
                break
            else:
                print("Insufficient payment. Try again.")
        except ValueError:
            print("Invalid Input. Please enter a valid amount.")


def generate_receipt(subtotal, tax, discount, total, amount_paid, change):
    # Prints a formatted receipt
    print("\n--- Best Buy Retail Store ---")
    print(" Sales Receipt")
    for item, quantity in cart.items():
        price = products[item][0]
        print(f"{item}: {quantity} x ${price} = ${price * quantity}")
    print(
        f"Subtotal: ${subtotal:.2f}\nSales Tax: ${tax:.2f}\nDiscount: ${discount:.2f}\nTotal Due: ${total:.2f}\nAmount Paid: ${amount_paid:.2f}\nChange: ${change:.2f}")
    print("Thank you for shopping with us!")


def main():
    # Main function to run the POS system
    while True:
        print("\n1. Add Item to Cart\n2. Remove Item\n3. View Cart\n4. Checkout\n5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            addCart()
        elif choice == '2':
            removeCart()
        elif choice == '3':
            viewCart()
        elif choice == '4':
            checkout()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()
