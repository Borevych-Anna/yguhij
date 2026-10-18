import schedule
import datetime


def schedule_task():
    def report_time():
        print("Запланований час:", datetime.datetime.now())

    schedule.every().day.at("12:00").do(report_time)

    print("Створено щоденне завдання на 12:00.")
    print("Кількість запланованих завдань:", len(schedule.get_jobs()))