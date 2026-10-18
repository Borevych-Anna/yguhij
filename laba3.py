products = [
    {"name": "Ноутбук асус таф геймінг ф17 крутий", "price": 33000.00, "amount": 5},
    {"name": "Чайник", "price": 2500.00, "amount": 10},
    {"name": "Дєшовка леново плашнет", "price": 12999.00, "amount": 7},
    {"name": "Холодос", "price": 50000.00, "amount": 4},
    {"name": "Іпхон 18 про макс", "price": 68000.00, "amount": 3}
]
cart = []

adm_login="Пікавару канон"
adm_password="483748"
price_format = lambda x: f"{x:.2f} грн"

def show_catalog():
    print("\nкаталог")
    for a, product in enumerate(products, 1):
        print(f"{a}. {product["name"]} - {price_format(product["price"])} - {product["amount"]} шт.")

def show_cart():
    print("\nкошик")
    if not cart:
        print("кошик пустий")
        return
    total = 0
    for a, i in enumerate(cart, 1):
        cost = i["price"] * i["amount"]
        total += cost
        print(f"{a}. {i["name"]} - {i["amount"]} шт. - {price_format(cost)}")
    print(f"разом: {price_format(total)}")

def add_to_cart():
    show_catalog()
    try:
        number = int(input("номер товару: "))
        quantity = int(input("кількість: "))
        if number < 1 or number > len(products):
            print("товар не знайдено")
            return
        product = products[number - 1]
        if quantity <= 0 or quantity > product["amount"]:
            print("неправильна кількість")
            return
        item = next((x for x in cart if x["name"] == product["name"]), None)
        if item:
            item["amount"] += quantity
        else:
            cart.append({
                "name": product["name"],
                "price": product["price"],
                "amount": quantity
            })
        print("товар добавлено")
    except ValueError:
        print("введіть число")

def remove_from_cart():
    show_cart()
    if not cart:
        return
    try:
        number = int(input("номер товару: "))
        quantity = int(input("кількість: "))
        if 1 <= number <= len(cart):
            item_index = number - 1
            item=cart[item_index]
            if quantity >= item["amount"]:
                cart.pop(item_index)
                print("товар повністю видалено")
            else:
                item["amount"] -= quantity
                print(f"товар видалено. залишилось: {item["amount"]}")
        else:
            print("Неправильний номер")
    except ValueError:
        print("введіть число")

def buy():
    if not cart:
        print("кошик порожній")
        return
    show_cart()
    answer = input("купити? (так/ні): ").lower()
    if answer == "так":
        for item in cart:
            for product in products:
                if product["name"] == item["name"]:
                    product["amount"] -= item["amount"]
        cart.clear()
        print("покупку здійснено")
    else:
        print("покупку скасовано")

def admin():
    login = input("логін: ")
    password = input("пароль: ")
    if login == adm_login and password == adm_password:
        print("\nвхід здійснено")
            admin_panel()
    else:
        print("неправильний логін або пароль")

def admin_panel():
    while True:
        print("\nпанель адміна")
        print("1. Переглянути залишки")
        print("2. Вийти")
        choice = input("Ваш вибір: ")
        if choice == "1":
            print("\nзалишки")
            sorted_products = sorted(
                products,
                key=lambda product: product["amount"]
            )
            for product in sorted_products:
                print(
                    f"{product["name"]} — "
                    f"{product["amount"]} шт."
                )
        elif choice == "2":
            break
        else:
            print("Невірний вибір.")

def main():
    while True:
        print("\nвітаємо у магазині")
        print("1. переглянути каталог")
        print("2. додати товар в кошик")
        print("3. переглянути кошик")
        print("4. видалити товар з кошика")
        print("5. купити товари")
        print("6. увійти як адміністратор")
        print("0. вийти з магазину")
        choice = input("ваш вибір: ")
        if choice == "1":
            show_catalog()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            show_cart()
        elif choice == "4":
            remove_from_cart()
        elif choice == "5":
            buy()
        elif choice == "6":
            admin()
        elif choice == "0":
            print("заходьте ще!")
            break
        else:
            print("невірний вибір")

if __name__ == "__main__":
    main()
