from src.bouquet.utility.printing import add_successfully, del_successfully, invalid_input


class FlowerInventory:

    def add_flower(self, menu):  # function for adding flower to dict...
        flower = input("Enter flower Name: ").upper()
        quantity = input("Enter Quantity : ")
        if quantity.isdigit():  # checking whether the quantity is number or not...if yes, then adding to dict...
            menu[flower] = quantity
            add_successfully()
        else:
            invalid_input()
            o1 = FlowerInventory
            o1.add_flower(self, menu)

    def del_flower(self, menu):  # function for deleting flower to dictionary...
        flower = input("Enter flower Name : ").upper()
        if flower in menu.keys():  # checking the flower is in dict or not...if yes, then deleting from dict...
            del menu[flower]
            del_successfully()
        else:
            invalid_input()
            o1 = FlowerInventory
            o1.del_flower(self, menu)

    def deducting_from_stock(self, menu, stock_bouquet):  # for deducting the quantity which is ordered
        key1 = []
        value1 = []
        for i in stock_bouquet:
            if i not in key1:
                key1.append(i)
                value1.append(stock_bouquet.count(i))

        d = dict(zip(key1, value1))
        for i in key1:
            menu[i] = menu[i] - d[i]
