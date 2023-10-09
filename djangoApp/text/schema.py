from datetime import datetime
from ninja import Schema

from content.schema import ContentRequestSchema,ContentResponseSchema



class TextRequestSchema(ContentRequestSchema):
    text: str
    
    

class TextResponseSchema(ContentResponseSchema):
    text: str