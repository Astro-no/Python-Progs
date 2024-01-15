names = []
with open('names.txt','r') as file:
    for line in file:
        line = line.strip()
        names.append(line)

nameRequested = input("What name can I find for you: ")
for name in names:
    if name.lower() == nameRequested.lower():
        print("I have found "+ name+ " in my list.")
        exit()
    
print("Sadly I did not find " + nameRequested + ".")

addName = input("Would you like to add " + nameRequested + "to the list of names? (Y/N)")    
if addName.lower == "y":
    names.append(nameRequested)
    print(nameRequested + " has been added to my list.")
    print(names)
else:
    print("Ok. I will not add " + nameRequested + "." )
    exit()

file = open("names.txt","a")
file.write(nameRequested + "\n")
file.close()
