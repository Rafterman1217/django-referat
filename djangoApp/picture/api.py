from typing import List
from ninja import Router

from content.schema import UpdateContentRequest

from .schema import PictureResponseSchema, PictureRequestSchema
from picture.models import Picture

router = Router()


@router.get("/", response=List[PictureResponseSchema])
def list_pictures(request):
    return Picture.objects.all()


@router.get("/{id}/", response=PictureResponseSchema)
def get_picture(request, id: int):
    return Picture.objects.get(id=id)


@router.post("/", response=PictureRequestSchema)
def create_picture(request, data: PictureRequestSchema):
    return Picture.objects.create(**data.dict())


@router.put("/{id}/", response=PictureRequestSchema)
def update_picture(request, id: int, data: UpdateContentRequest):
    picture = Picture.objects.get(id=id)
    for attr, value in data.dict().items():
        if value is not None:
            setattr(picture, attr, value)

    picture.save()
    return picture


@router.delete("/{id}/")
def delete_picture(request, id: int):
    Picture.objects.get(id=id).delete()
    return {"success": True}
