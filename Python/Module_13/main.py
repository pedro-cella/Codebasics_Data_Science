from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/")
def hello():
    return "Hello World"

@app.get("/hello/{name}")
def hello(name):
    return f"Hello {name}"

food_items = {
    'indian': ["Samosa", "Dosa"],
    'american': ["Hot Dog", "Apple Pie"],
    'italian': ["Ravioli", "Pizza"]
}

class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"

# Without using a class
# @app.get("/get_items/{cuisine}")
# def get_items(cuisine):
#     items = food_items.get(cuisine)
#     if not items:
#         return f"{cuisine} cuisine is not available"
#     return food_items.get(cuisine)

# Using a class
@app.get("/get_items/{cuisine}")
def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine)

coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/get_coupon/{code}")
async def get_items(code: int):
    return {'discount_amount': coupon_code.get(code)}