from data.data import Person
import random

from faker import Faker

faker_en = Faker('en_US')


def generated_person():
    return Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        firstname=faker_en.first_name(),
        lastname=faker_en.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker_en.job(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address(),
        mobile=faker_en.msisdn(),
    )

adr = generated_person().current_address
print(adr)