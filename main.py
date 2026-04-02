name = input("Enter customer name: ")
all_items = 0
subtotal = 0.0

while True:
    item_name = input("Enter item name(or 'done' to finish): ")

    if item_name == "done":
        break

    price = float(input("Enter item price: "))
    all_items += 1
    subtotal += price

print(f"Customer: {name.upper()}")
print(f"Items: {all_items}")
print(f"Subtotal: {subtotal} KZT")

hour = int(input("Enter current hour (0-23): "))

percents_off = 0
time_period = ""

if 6<=hour<12:
    percents_off = 10
    time_period = "Morning discount"
elif 12 <= hour < 17:
    percents_off = 0
    time_period = ("No discount")
elif 17 <= hour < 22:
    percents_off = 5
    time_period = "Evening discount"
else:
    print("Closed")
    exit()

discount = subtotal * (percents_off/100)
with_discount = subtotal - discount
tip =  with_discount * 0.1
total = tip + with_discount


print("-" * 30)
print(f"\nTime period: {time_period}")
print(f"Discount: {discount} KZT")
print(f"Tip (10%) : {tip} KZT")
print(f"Total : {total} KZT\n")
print("-" * 30)

print(f"Name uppercase: {name.upper()}")
print(f"Name lowercase: {name.lower()}")
print(f"Name length: {len(name)}")

if name[0].upper() == 'A' or name[0].upper() == 'S':
    print("VIP customer")
else:
    print("Regular customer")






