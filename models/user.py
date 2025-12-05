from pathlib import Path


class User:
    def __init__(
            self,
            first_name: str,
            last_name: str,
            email: str,
            phone: str,
            gender: str,
            birth_day: str,
            birth_month: str,
            birth_year: str,
            subjects: list[str],
            hobbies: list[str],
            address: str,
            state: str,
            city: str,
            file_path: Path,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.gender = gender

        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year

        self.subjects = subjects
        self.hobbies = hobbies

        self.address = address
        self.state = state
        self.city = city

        self.file_path = file_path
        self.file_name = file_path.name

    def __repr__(self):
        return f"User({self.first_name} {self.last_name})"