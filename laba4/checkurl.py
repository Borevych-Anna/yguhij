import validators


def check_url(url):
    if validators.url(url):
        print(f"Посидання коректне: {url}")
    else:
        print(f"Посилання некоректне: {url}")