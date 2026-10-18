from faker import Faker
import random

fake = Faker()


def generate_user():
    user = {
        "name": fake.name(),
        "email": fake.email(),
        "city": fake.city(),
        "age": random.randint(1, 80)
    }

    return user