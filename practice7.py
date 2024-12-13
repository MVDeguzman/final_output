buy =input("did you buy grocery? yes or no: ")

if buy.lower() == "yes":
      print("fill the information bellow")
else:
    print('thank you fpor using teh system')
    
item = input("name of the item: ")

#list of product
it1 = "pork"
it2 = "milk"
it3 = "chicken"
it4 = "beef"

if item == it1:
        print("the price of item is: 250.00")

elif item == it2:
        print("the price of item is: 250.00")

elif item == it3:
        print("the price of item is 250.00")

elif item == it4:
        print("the price of item is 250.00")
    

else:
    print("the item is not available")
    
amount = int(input("enter the amount: "))

#computation for discount
disc1 = 13
amt1 = 250 - disc1
exc1 = amount - amt1

#computation for tax
disc2 = 30.75
amt2 = 250 + disc2
exc2 = amount - amt2

age= int(input("enter your age: "))

if age >= 60 and amount:
    print("hi customer, you purchased a", item, "with a price of 250.000 discounted by 5.2%", {disc1} )
    print("total of: ", amt1)
    print("amount given: " , amount)
    print("change: " , exc1 )

elif age < 60 and amount:
    print("hi customer, you purchased a", item, "with a price of 250.000 plus 12.3% tax ",{disc2} )
    print("total of: ", amt2)
    print("amount given: " , amount)
    print("change: " , exc2)

else:
    print("you have no voucher")






