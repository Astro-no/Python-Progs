
def toupper(text):
    return text.upper()

with open('Cofee Records.txt', 'w') as file:
    while True:
        product_description = input("Enter the Product description (or 'exit' to stop adding records): ")
        if product_description.lower() == 'exit':
            break
        product_quantity = input("Enter the product quantity: ")
        file.write(f"{product_description}, {product_quantity}\n") 


file.close()


try:
    with open('Cofee Records.txt', 'r') as file:
        print("All Records in the Inventory:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("The file 'Cofee Records.txt' does not exist or cannot be opened.")
