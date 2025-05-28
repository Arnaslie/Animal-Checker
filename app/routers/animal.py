from fastapi import APIRouter, HTTPException, File, UploadFile
import torch
from transformers import pipeline
from PIL import Image
import io
from .sonar import realtime_request

pipeline = pipeline(
    task="image-classification",
    model="google/vit-base-patch16-224",
    torch_dtype=torch.float16,
    device=0
)

router = APIRouter(
    prefix="/animal",
    tags=["animal"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def check_animal():
    return {'animal': 'dog'}

@router.post("/file/{location}")
async def inspect_image(file: UploadFile, location: str):
    try:
        request_object_content = await file.read()
        img = Image.open(io.BytesIO(request_object_content))
        print(f"Image format: {img.format}")
        print(f"Image size: {img.size}")
        if pipeline is not None:
            scores = pipeline(images=img)
            resp = realtime_request(scores[0]['label'], location)
            return resp
        else:
            return 'no'
    except Exception as e:
        return {"message": f"Error processing image: {e}"}
