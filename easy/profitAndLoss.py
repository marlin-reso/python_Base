def findProfitOrLoss():
    cost_price = int(input("Enter cost price of item : "))
    selling_price = int(input("Enter the selling price of item : "))
    if cost_price == selling_price:
        return("not profit nor loss")
    elif cost_price>selling_price:
        loss = ((cost_price-selling_price)*100)/cost_price
        print(f"you are in {loss}% loss")
    elif selling_price>cost_price:
        profit = ((selling_price-cost_price)*100)/cost_price
        print(f"you are in {profit}% profit")
    else:
        print("invalid argument")
findProfitOrLoss()