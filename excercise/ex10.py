def give_ticket_by_categorie(cat: str, price: float, amount: int) -> str:
    if amount != 0:
        avg: float = price / amount
    else:
        avg = 0

    s = f"{amount} products are in the category {cat}\naverage: {avg:.2f}"
    return s


bev_tot = 0
bev_am = 0
frt_tot = 0
frt_am = 0
veg_tot = 0
veg_am = 0

amount = int(input("Specify the number of products you wish to enter: "))

for i in range(amount):
    cat = input("What is the category? [V: Vegetables, F: Fruit, B: Beverages]: ").upper()
    cos = float(input("What is the cost price of the product: "))

    if cat == "V":
        veg_tot += cos
        veg_am += 1

    elif cat == "B":
        bev_tot += cos
        bev_am += 1

    elif cat == "F":
        frt_tot += cos
        frt_am += 1

    else:
        print("Invalid category!")

print(give_ticket_by_categorie("Vegetables", veg_tot, veg_am))
print(give_ticket_by_categorie("Fruit", frt_tot, frt_am))                                                                                                                    