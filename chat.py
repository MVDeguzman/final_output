pre = float(input("Please enter your grade in prelim: "))

weighted_grade = pre * 0.15

if 75 >= weighted_grade <= 100:
    print("You passed the prelim")
else:
    print("You failed")