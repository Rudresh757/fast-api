from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"hello customer"}
class Book(BaseModel):
    book_name: str
    book_author: str
    book_price: float
    book_serial_number: int

@app.post("/book")
def create_book(book:Book)