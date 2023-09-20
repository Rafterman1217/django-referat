from typing import List
from ninja import Router, Schema

from content.schema import UpdateContentRequest


from .schema import TextSchema
from text.models import Text

router = Router()

@router.get("/", response=List[TextSchema])
def list_texts(request):
    return Text.objects.all()

@router.get("/{id}/", response=TextSchema)
def get_text(request, id: int):
    return Text.objects.get(id=id)

@router.post("/", response=TextSchema)
def create_text(request, data: TextSchema):
    return Text.objects.create(**data.dict())

@router.put("/{id}/", response=TextSchema)
def update_text(request, id: int, data: UpdateContentRequest):
    text = Text.objects.get(id=id)
    
    for attr, value in data.dict().items():
        if value is not None:
            setattr(text, attr, value)
    
    text.save()
    return text

@router.delete("/{id}/")
def delete_text(request, id: int):
    Text.objects.get(id=id).delete()
    return {"success": True}
