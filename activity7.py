gold = 0
miner = input("hi, what is your name? ")
isgold = input("the mineral is gold?")

if isgold == "yes":
    gold += 1
    print(f" Hi", miner , "Your total of gold is", gold)

else:
    print(f"Hi", miner , "Your total number of gold is", gold)
               