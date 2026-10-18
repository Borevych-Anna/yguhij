from generateuser import generate_user
from createimage import create_image
from analyzenumbers import analyze_numbers
from plotdata import plot_data
from printtable import print_tabulate
from makeqr import make_qr
from checkurl import check_url
from scheduletask import schedule_task
from showemoji import show_emoji
from bannerr import banner
from savejson import save_json
from currenttime import current_time
from randomnumber import random_number
from ensurefolder import ensure_folder
from calculatee import calculate


def main():
    ensure_folder("output")

    user = generate_user()
    print_tabulate(user)

    create_image(user["name"])
    analyze_numbers()
    plot_data()
    make_qr("https://www.python.org")
    check_url("https://www.python.org")

    schedule_task()
    show_emoji()
    banner()

    save_json(user, "output/user.json")
    current_time()
    random_number()
    calculate()

    print("\nУсі операції завершено!")


if __name__ == "__main__":
    main()