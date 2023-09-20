from typing import List
from ninja import Router, Schema

from content.schema import UpdateContentRequest

from .schema import PictureSchema
from picture.models import Picture

router = Router()



@router.get("/pictures/", response=List[PictureSchema])
def list_pictures(request):
    return Picture.objects.all()

@router.get("/pictures/{id}/", response=PictureSchema)
def get_picture(request, id: int):
    return Picture.objects.get(id=id)

@router.post("/pictures/", response=PictureSchema)
def create_picture(request, data: PictureSchema):
    return Picture.objects.create(**data.dict())

@router.put("/pictures/{id}/", response=PictureSchema)
def update_picture(request, id: int, data: UpdateContentRequest):
    picture = Picture.objects.get(id=id)
    
    # Update nur die Felder, die im Request angegeben sind
    for attr, value in data.dict().items():
        if value is not None:
            setattr(picture, attr, value)
    
    picture.save()
    return picture

@router.delete("/pictures/{id}/")
def delete_picture(request, id: int):
    Picture.objects.get(id=id).delete()
    return {"success": True}
