from datetime import datetime
from ninja import Schema

from content.schema import ContentRequestSchema,ContentResponseSchema



class PictureRequestSchema(ContentRequestSchema):
    picture: str  

class PictureResponseSchema(ContentResponseSchema):
    picture: str  
