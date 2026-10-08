class Refrigerator:

    def __init__(self, name, price, capacity, manufacturer):
        self.name = name
        self.price = price
        self.capacity = capacity
        self.manufacturer = manufacturer


def save_refrigerators(filename, items):
    with open(filename, "w", encoding="utf-8") as file:
        for item in items:
            file.write(
                f"{item.name},{item.price},{item.capacity},{item.manufacturer}\n"
            )


def load_refrigerators(filename):
    items = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    items.append(
                        Refrigerator(
                            parts[0],
                            float(parts[1]),
                            float(parts[2]),
                            parts[3],
                        )
                    )
    except FileNotFoundError:
        print("File not found.")
    return items


def main():
    filename = "refrigerators.txt"
    count = int(input("Enter number of refrigerators: "))
    items = []

    for i in range(count):
        print(f"\nRefrigerator #{i + 1}:")
        name = input("Name: ")
        price = float(input("Price: "))
        capacity = float(input("Freezer capacity (L): "))
        manufacturer = input("Manufacturer: ")
        items.append(Refrigerator(name, price, capacity, manufacturer))

    save_refrigerators(filename, items)
    loaded_items = load_refrigerators(filename)

    print("\n--- Refrigerators with price > 55000 UAH ---")
    print(f"{'Name':<15} {'Price':<12} {'Capacity':<12} {'Manufacturer':<15}")
    print("-" * 54)
    for item in loaded_items:
        if item.price > 55000:
            print(
                f"{item.name:<15} {item.price:<12.2f} {item.capacity:<12.1f} {item.manufacturer:<15}"
            )


if __name__ == "__main__":
    main()