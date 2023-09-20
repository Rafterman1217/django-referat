from ninja import NinjaAPI
from picture.api import router as PictureRouter
from text.api import router as TextRouter


api = NinjaAPI()
api.add_router("pictures/",PictureRouter,tags=["Pictures"])
api.add_router("texts/",TextRouter,tags=["Texts"])
