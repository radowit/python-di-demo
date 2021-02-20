from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Ticket:
    ticket_id: int
    creation_time: datetime = field(default_factory=datetime.now)
