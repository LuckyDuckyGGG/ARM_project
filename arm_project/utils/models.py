from dataclasses import dataclass
from typing import Optional

@dataclass
class ProjectData:
    name: str
    short_name: str
    code: str
    start_date: str
    end_date: str
    deadline_remark: str
    country: str
    city: str
    street: str
    building: str
    office: str
    postal_code: str
    responsible_email: Optional[str] = None