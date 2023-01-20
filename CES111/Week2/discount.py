import datetime

customer_subtotal = float(input("What is the subtotal amount? "))
while True:
    def calculate_sales_tax(subtotal_with_discount):
        tax_amount = subtotal_with_discount * .06
        total_with_tax = tax_amount + subtotal_with_discount
        return total_with_tax, tax_amount

    def calculate_discount(current_day, customer_subtotal):
        if current_day == "tuesday" or current_day == "wednesday":
            discount = customer_subtotal * .10
            discount_percent = int(discount)
            print(f"You get a discount of 10% because your order was at or over $50 and is on a Tuesday or a Wednesday. The amount of this discount is {discount_percent}%")
        else:
            discount = 0
            remaining_amount_to_get_a_discount = 50 - customer_subtotal
            print(f"Your purchase does not qualify for a discount. You need to spend ${remaining_amount_to_get_a_discount} more to get a discount and purchase on a Tuesday or Wednesday.")
        return discount

    current_day_raw = datetime.datetime.now()
    current_day = (current_day_raw.strftime("%A")).lower()
    discount_day = calculate_discount(current_day=current_day, customer_subtotal=customer_subtotal)
    calculated_sales_tax = calculate_sales_tax(customer_subtotal)
    total_amount_owed = customer_subtotal - discount_day + calculated_sales_tax[1]

    print(f"A sales tax of 6% is assesed on the total. With the sales tax amount added. Total is ${calculated_sales_tax[0] :.2f}")
    print(f"Your discounted amount is ${discount_day :.2f}. With this discount added your total owed is ${total_amount_owed :.2f}")
    print("")
    customer_subtotal = float(input("If there is another amount you would like to calculate, enter it now. If not, enter 0 to exit: "))
    if customer_subtotal == 0:
        print("sub toal is $0. Program does not need to run")
        break