from pathlib import Path

from faker import Faker

from models.user import User

fake = Faker()
Faker.seed(123)

ROOT = Path(__file__).resolve().parents[1]


class UserFactory:
    @staticmethod
    def create() -> User:
        first = fake.first_name()
        last = fake.last_name()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=60)

        return User(
            first_name=first,
            last_name=last,
            email=fake.email(),
            phone=fake.msisdn()[:10],
            gender=fake.random_element(["Male", "Female"]),
            birth_day=str(birthday.day),
            birth_month=birthday.strftime("%B"),
            birth_year=str(birthday.year),
            subjects=[fake.random_element(["Maths", "Physics", "Biology", "English"])],
            hobbies=[fake.random_element(["Sports", "Reading", "Music"])],
            address=fake.address().replace("\n", " "),
            state="NCR",
            city="Delhi",
            file_path=ROOT / "tests" / "resources" / "image.png",
        )
