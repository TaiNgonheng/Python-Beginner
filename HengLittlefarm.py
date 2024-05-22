print(("*" * 40))
print("Welcome to my Shop🙋")
print("1: Apple🍎 (💵: 5000r)")
print("2: Grape🍇 (💵: 6000r)")
print("3: Melon🍈 (💵: 8000r)")
print("4: Orange🍊 (💵: 2000r)")
print(("*" * 40))
Item = int(input("Enter the number (between 1 to 4): "))
if Item <=4:
    if Item == 1:
        fruit = "Apple"
        price = 5000
        sticker = "🍎"
    elif Item == 2:
        fruit = "Grape"
        price = 6000
        sticker = "🍇"

    elif Item == 3:
        fruit ="Melon"
        price = 8000
        sticker ='🍈'
    else:
        fruit = "Orange"
        price = 2000
        sticker = "🍊"
    Quantity = int(input("Enter the Quantity of Item (between 1 to 10): "))
    if Quantity <=10:
        print("Fruit selected: ",fruit,sticker,sep="")
        print("price: ",price,"💵")
        print("Quantity: ",Quantity*sticker,sep=" ")
        total = price*Quantity
        print("Total price is: ",total,"💵",sep="")
        insert_money = int(input("Insert money please: "))
        if insert_money < total:
            print("not correct")
            while insert_money < total:
                insert_money = int(input("Insert money please to cover total: "))
            change = insert_money - total
            print(insert_money,("💵 received. Your change is: "),change,('💵'),sep="")
            print(("*" * 40))
        else:
            change = insert_money - total
            print(insert_money,("💵 received. Your change is: "),change,('💵'),sep="")
            print(("*" * 40))
        print("\t\t\t\t\t\t\t\t\t\t\t\t\tHere is Yours: ",sticker*Quantity,sep="")
    else:
        while Quantity>10:
            print("We can't sell over 10.🙏")
            Quantity = int(input("Enter the Quantity of Item (between 1 to 10): "))
        print("Fruit selected: ", fruit, sticker, sep="")
        print("price: ", price, "💵")
        print("Quantity: ", Quantity * sticker, sep=" ")
        total = price * Quantity
        print("Total price is: ", total, "💵", sep="")
        insert_money = int(input("Insert money please: "))
        if insert_money < total:
            print("not correct")
            while insert_money < total:
                insert_money = int(input("Insert money please to cover total: "))
            change = insert_money - total
            print(insert_money, ("💵 received. Your change is: "), change, ('💵'), sep="")
            print(("*" * 40))
        else:
            change = insert_money - total
            print(insert_money, ("💵 received. Your change is: "), change, ('💵'), sep="")
            print(("*" * 40))
        print("\t\t\t\t\t\t\t\t\t\t\t\t\tHere is Yours: ", sticker * Quantity, sep="")
else:
    while Item > 4:
        print("We have only 4 fruits in stock.")
        Item = int(input("Enter the number (between 1 to 4): "))
        if Item <= 4:
            if Item == 1:
                fruit = "Apple"
                price = 5000
                sticker = "🍎"
            elif Item == 2:
                fruit = "Grape"
                price = 6000
                sticker = "🍇"

            elif Item == 3:
                fruit = "Melon"
                price = 8000
                sticker = '🍈'
            else:
                fruit = "Orange"
                price = 2000
                sticker = "🍊"
            Quantity = int(input("Enter the Quantity of Item (between 1 to 10): "))
            if Quantity <= 10:
                print("Fruit selected: ", fruit, sticker, sep="")
                print("price: ", price, "💵")
                print("Quantity: ", Quantity * sticker, sep=" ")
                total = price * Quantity
                print("Total price is: ", total, "💵", sep="")
                insert_money = int(input("Insert money please: "))
                if insert_money < total:
                    print("not correct")
                    while insert_money < total:
                        insert_money = int(input("Insert money please to cover total: "))
                    change = insert_money - total
                    print(insert_money, ("💵 received. Your change is: "), change, ('💵'), sep="")
                    print(("*" * 40))
                else:
                    change = insert_money - total
                    print(insert_money, ("💵 received. Your change is: "), change, ('💵'), sep="")
                    print(("*" * 40))
                print("\t\t\t\t\t\t\t\t\t\t\t\t\tHere is Yours: ", sticker * Quantity, sep="")
            else:
                while Quantity > 10:
                    print("We can't sell over 10.🙏")
                    Quantity = int(input("Enter the Quantity of Item (between 1 to 10): "))
                    print("Fruit selected: ", fruit, sticker, sep="")
                    print("price: ", price, "💵")
                    print("Quantity: ", Quantity * sticker, sep=" ")
                    total = price * Quantity
                    print("Total price is: ", total, "💵", sep="")
                    insert_money = int(input("Insert money please: "))
                    if insert_money < total:
                        print("not correct")
                        while insert_money < total:
                            insert_money = int(input("Insert money please to cover total: "))
                        change = insert_money - total
                        print(insert_money, ("💵 received. Your change is: "), change, ('💵'), sep="")
                        print(("*" * 40))
                    else:
                        change = insert_money - total
                        print(insert_money, ("💵 received. Your change is: "), change, ('💵'), sep="")
                        print(("*" * 40))
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\tHere is Yours: ", sticker * Quantity, sep="")