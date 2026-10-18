import datetime


def current_time():
    now = datetime.datetime.now()

    print("Поточна дата:", now.strftime("%d.%m.%Y"))
    print("Поточний час:", now.strftime("%H:%M:%S"))