from fastapi import APIRouter

router = APIRouter()

@app.get("/animal")
def check_animal(animal: str):
    return 'animal'