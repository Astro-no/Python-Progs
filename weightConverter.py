weight = int(input("Enter your weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    converted = weight / 0.45
    print("Your weight in Lbs: " + str(converted))

else:
    converted = weight * 0.45
    print("Your weight in Kgs: " + str(converted))    
