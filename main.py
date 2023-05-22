from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


#uvicorn main:app --host 2607:fea8:1f1c:6600::12 --port 8000 --reload
#uvicorn main:app --port 8000 --reload