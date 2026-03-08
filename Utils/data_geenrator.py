from faker import Faker
import random

fake = Faker()


class DataGenerator:
    # Generuje poprawne imię i nazwisko
    # Formularz wymaga, aby pole nie było puste
    def name(self):
        return fake.name()

    # Generuje poprawny email
    # Formularz wymaga, aby email nie był pusty
    def email(self):
        return fake.email()

    # Generuje numer telefonu o długości 11–21 znaków
    # Formularz wymaga min. 11 i max. 21 znaków
    # https://docs.python.org/3.14/library/random.html#random.randint
    def phone(self):
        length = random.randint(11, 21)
        return ''.join(str(random.randint(0, 9)) for _ in range(length))

    # Generuje temat wiadomości (subject)
    # Formularz wymaga min. 5 znaków
    def subject(self):
        # 3 słowa dają zwykle 15–25 znaków
        return fake.sentence(nb_words=3)

    # Generuje treść wiadomości
    # Formularz wymaga min. 20 znaków
    def message(self):
        # Tekst do 200 znaków — zawsze spełnia minimum 20
        return fake.text(max_nb_chars=200)
