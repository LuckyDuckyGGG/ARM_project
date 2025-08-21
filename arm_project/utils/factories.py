import random
from faker import Faker
from datetime import datetime, timedelta

from arm_project.utils.models import *
fake = Faker('ru_RU')


class ProjectFactory:

    def create_project(self, **kwargs) -> ProjectData:
        random_number = random.randint(1, 999)
        start_date = datetime.now() + timedelta(days=random.randint(1, 30))
        end_date = start_date + timedelta(days=random.randint(1, 365))

        default_data = {
            'name': f"Проект{random_number}",
            'short_name': f"Пр.{random_number}",
            'code': f"№{random_number}",
            'start_date': start_date.strftime("%d-%m-%Y"),
            'end_date': end_date.strftime("%d-%m-%Y"),
            'deadline_remark': str(random_number),
            'country': fake.country(),
            'city': fake.city_name(),
            'street': fake.street_name(),
            'building': fake.building_number(),
            'office': str(random_number),
            'postal_code': fake.postcode(),
        }

        default_data.update(kwargs)
        return ProjectData(**default_data)

class UserFactory:

    def create_user(self, **kwargs):
        user_data = {
            "name": fake.first_name(),
            "last_name": fake.last_name(),
            "middle_name": fake.middle_name(),
            "phoneNumber": fake.phone_number(),
            "password": fake.password(length=8)
        }

        user_data.update(kwargs)

        return User(**user_data)