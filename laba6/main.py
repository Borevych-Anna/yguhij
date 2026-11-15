from decorators import capitalize_decorator

def get_greeting(name):
    return f"Хай, {name}))"

def get_status_message():
    return "Все гуд"

get_greeting = capitalize_decorator(get_greeting)
get_status_message = capitalize_decorator(get_status_message)

if __name__ == "__main__":
    main()