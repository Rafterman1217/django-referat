from ninja import Schema
from datetime import datetime

class ContentSchema(Schema):
    id: int
    created_at: datetime
    show_until: datetime
    show_since: datetime
    

class UpdateContentRequest(Schema):
    show_until: datetime = None
    show_since: datetime = None