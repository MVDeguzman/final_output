buy =input("did you buy grocery? yes or no: ")

price = 250.00


if buy.lower() == "yes":
    print("item available:")
    print("-pork")
    print("-milk")
    print("-chicken")
    print("-beef")
    ans= print("answer the needed below") 
else:
    print("error")


if buy.lower() == "yes":
    items = ["pork", "milk", "chicken", "beef"]
    
    item = input("name of the item: ")

    if item in items:
        print("the price of item is: 250.00")

    else:
        print("item not found")
else:
    print("error")
    
if  buy.lower() == "yes":
    print("the price of the item is: ", price)
    amount = int(input("enter the amount: "))
    age= int(input("enter your age: "))

    discount = round((price *0.052), 2)

    total = price - discount

    exc = amount - total

    tax = round((price * 0.123), 2)
    total2 = price + tax
    exc2 = amount - total
    
    if age >= 60 and amount:
        print("hi customer, you purchased a", item, "with a price of 250.000 discounted by 5.2%", discount )
        print(f"total of: {total},")
        print("amount given: " , amount)
        print("change: " , exc )

    elif age < 60 and amount:
        print("hi customer, you purchased a", item, "with a price of 250.000 plus 12.3% tax ", tax )
        print("total of: ", total2)
        print("amount given: " , amount)
        print("change: " , exc2)

else:
    print("error")






