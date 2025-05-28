from fastapi import FastAPI
from .routers import animal

app = FastAPI()
app.include_router(animal.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

def main():
    print("Hello from hackathon!")

if __name__ == "__main__":
    main()
