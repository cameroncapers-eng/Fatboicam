# 1. Create a list of items in your room you can potentially pack.
room_items = [
    "Shirt",
    "Pants",
    "Shoes",
    "Laptop",
    "Phone Charger",
    "Toothbrush",
    "Book",
    "Headphones",
    "candle",
    "Notebook"

]


def create_travel_bag(room_items):
    travel_bag = []

    print("Items in your room:")
    for i, item in enumerate(room_items):
        print(f"{i}: {item}")


    while room_items:
        choice = input("\nEnter the index of an item to pack (or 'done' to finish): ")

        if choice.lower() == "done":
            break

        try:
            index = int(choice)
            if 0 <= index < len(room_items):
                item = room_items.pop(index)
                travel_bag.append(item)
                print(f"Packed: {item}")

                print("\nRemaining items:")
                for i, item in enumerate(room_items):
                    print(f"{i}: {item}")
            else:
                print("Invalid index.")
        except ValueError:
            print("Please enter a valid number or 'done'.")
    return travel_bag

travel_bag = create_travel_bag(room_items)


luggage = ()

while travel_bag:
    luggage += (travel_bag.pop(0),)


print("\nYour luggage contains:")
for item in luggage:
    print("-", item)

print(f"\nTotal items packed: {len(luggage)}")