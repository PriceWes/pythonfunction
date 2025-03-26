def calculate_discount(price, discount_percent):
    discount = price*discount_percent/100
    if discount_percent >= 20:
        newprice = price - discount
        return newprice
    else:
        return price


try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    newprice = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Your discounted price is: {newprice:.2f}")
    else:
        print(f"No discount applied. The price is: {price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
