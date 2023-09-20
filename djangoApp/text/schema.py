from datetime import datetime
from ninja import Schema

from content.schema import ContentSchema


class TextSchema(ContentSchema):
    text: str