from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# Định nghĩa các service URL
CUSTOMER_SERVICE_URL = "http://127.0.0.1:8000/api"
ITEM_SERVICE_URL = "http://127.0.0.1:8001/api"
CART_SERVICE_URL = "http://127.0.0.1:8002/api"

# Định tuyến cho Customer_Service
@app.post("/api/customers/")
async def create_customer(data: dict):
    response = requests.post(f"{CUSTOMER_SERVICE_URL}/customers/", json=data)
    return response.json()

@app.get("/api/customers/all/")
async def get_all_customers():
    response = requests.get(f"{CUSTOMER_SERVICE_URL}/customers/all/")
    return response.json()

# Định tuyến cho Item_Service
@app.get("/api/items/all/")
async def get_all_items():
    response = requests.get(f"{ITEM_SERVICE_URL}/items/all/")
    return response.json()

# Định tuyến cho Cart_Service
@app.post("/api/carts/")
async def create_cart(data: dict):
    response = requests.post(f"{CART_SERVICE_URL}/carts/", json=data)
    return response.json()

@app.post("/api/carts/{cartId}/add-item/")
async def add_item_to_cart(cartId: str, data: dict):
    response = requests.post(f"{CART_SERVICE_URL}/carts/{cartId}/add-item/", json=data)
    return response.json()

@app.get("/api/carts/{cartId}/items/")
async def get_all_items_in_cart(cartId: str):
    response = requests.get(f"{CART_SERVICE_URL}/carts/{cartId}/items/")
    return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)