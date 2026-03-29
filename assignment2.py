name = input("Enter customer name: ")
item1_name = input("Enter name of item 1: ")
item1_price = int(input("Enter price of item 1(KZT): "))
item2_name = input("Enter name of item 2: ")
item2_price = int(input("Enter price of item 2(KZT): "))
people = int(input("Enter number of people: "))

subtotal = item1_price + item2_price
tip = subtotal * 0.1
total = subtotal + tip
per_person = total / people

print("=" * 30)
print(" " * 10 + "CAFE BILL")
print("=" * 30)
print("Customer: ", name)
print(item1_name + ": " + str(item1_price) + " KZT")
print(item2_name + ": " + str(item2_price) + " KZT")
print("Subtotal: " + str(subtotal) + " KZT")
print("Tip (10%): " + str(tip) + " KZT")
print("Total: " + str(total) + " KZT")
print("Per person: " + str(per_person) + " KZT")
print("=" * 30)

if tip > 0:
    print("Tip included: True")


if total > 5000:
    print("Bill over 5000 KZT: True")