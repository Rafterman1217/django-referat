from typing import List
from ninja import Router

from content.schema import UpdateContentRequest


from .schema import TextRequestSchema, TextResponseSchema
from text.models import Text

router = Router()


@router.get("/", response=List[TextResponseSchema])
def list_texts(request):
    return Text.objects.all()


@router.get("/{id}/", response=TextResponseSchema)
def get_text(request, id: int):
    return Text.objects.get(id=id)


@router.post("/", response=TextRequestSchema)
def create_text(request, data: TextRequestSchema):
    return Text.objects.create(**data.dict())


@router.put("/{id}/", response=TextRequestSchema)
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
