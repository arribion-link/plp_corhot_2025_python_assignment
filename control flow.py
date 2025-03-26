#calculate price of item after apppling the discount

price = int(input("PLEASE ENTER THE PRICE OF THE ITEM: "))

def calculate_discount(price, discount_percentage):
    #calculating the discount of 20%
    x = price * 80
    discount_percentage = x / 100

    return discount_percentage

print("THE 20% DISCOUNT OF ITEM IS: ", calculate_discount())


