def breakdown_denomination(amount):
    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    result = {}
    
    for denomination in denominations:
        count = amount // denomination
        amount %= denomination
        if count > 0:
            result[denomination] = count
    
    print("Breakdown ng Denomination:")
    for denomination, count in result.items():
        print(f"{denomination}: {count}")