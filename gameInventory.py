stuff = {'pound': 1000, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 120}

def display_inventory(inventory):
    print("Inventory:")
    itemTotal = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        itemTotal = item_total + v
    print("Total number of items: " + str(itemTotal))

display_inventory(stuff)
