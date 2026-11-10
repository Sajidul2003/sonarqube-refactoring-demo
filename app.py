DEFAULT_TAX_RATE = 0.15


# Example 1: Hidden dependency
def calculate_total(price, quantity):
    subtotal = price * quantity
    tax = subtotal * DEFAULT_TAX_RATE
    return subtotal + tax


# Example 2: Unused parameter
def create_invoice(customer_name, customer_id, amount):
    return f"Invoice for {customer_name}: {amount}"


# Example 3: Mysterious method name
def do_stuff(price, discount):
    return price - (price * discount)


# Main program
total = calculate_total(100, 2)
invoice = create_invoice("Rahim", 101, total)
final_price = do_stuff(1000, 0.10)

print("Total:", total)
print(invoice)
print("Final Price:", final_price)
