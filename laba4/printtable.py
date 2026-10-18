from tabulate import tabulate


def print_tabulate(user):
    rows = [
        ["Ім'я", user["name"]],
        ["Email", user["email"]],
        ["Місто", user["city"]],
        ["Вік", user["age"]],
    ]

    print(tabulate(rows, headers = ["", ""], tablefmt = "grid"))