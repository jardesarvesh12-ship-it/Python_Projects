menu = {
    "Burger" : 70,
    "pizza" : 110,
    "peri peri frize" : 85,
    "pasta" : 150,
    "coke" : 50,
    "cold coffe" : 30
}

print("Welecome to SM18 Cafe: ")
print("Menu:- \nBurger:70rs\npizza:110rs\nperi peri frize:85rs\npasta:150rs\ncoke:50\ncold coffe:30")


total_order = 0

item1 = input("hello ,order please: ")
if item1 in menu:
    total_order += menu[item1]
    print(f"you food {item1} is add to the order")
else:
    print(f"{item1} not in stock")


another_order = input("Any think else to eat? (yes/No)")
if another_order == "yes":


    item2 = input("please tell me the another order")
    if item2 in menu:
        total_order += menu[item2]
        print(f"your item {item2}is added: ")
    else:
        print(f" {item2}not in stock")

print(f"Total amount of your food is: ", total_order)