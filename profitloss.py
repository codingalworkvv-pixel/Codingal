cost_price = int(input("Enter Cost of Item:"))
sell_price = int(input("What is the selling price of this item? "))
if sell_price < cost_price:
    print("Loss", cost_price - sell_price)
elif sell_price == cost_price:
    print("Break Even")
else:
    print("Profit", sell_price - cost_price)