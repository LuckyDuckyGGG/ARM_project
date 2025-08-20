import random
from faker import Faker
from datetime import datetime, timedelta

from arm_project.utils.models import ProjectData


class ProjectFactory:
    def __init__(self, locale='ru_RU'):
        self.fake = Faker(locale)

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
            'country': self.fake.country(),
            'city': self.fake.city_name(),
            'street': self.fake.street_name(),
            'building': self.fake.building_number(),
            'office': str(random_number),
            'postal_code': self.fake.postcode(),
        }

        default_data.update(kwargs)
        return ProjectData(**default_data)