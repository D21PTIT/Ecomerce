from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CUSTOMER_SERVICE_URL = "http://127.0.0.1:8000/api"
ITEM_SERVICE_URL = "http://127.0.0.1:8001/api"
CART_SERVICE_URL = "http://127.0.0.1:8002"
PAYMENT_SERVICE_URL = "http://127.0.0.1:8003/api"
SHIPMENT_SERVICE_URL = "http://127.0.0.1:8004/api"
ORDER_SERVICE_URL = "http://127.0.0.1:8005/api"
ADMIN_SERVICE_URL = "http://127.0.0.1:8006/api"

# Customer_Service
@app.post("/api/customers/")
async def create_customer(data: dict):
    response = requests.post(f"{CUSTOMER_SERVICE_URL}/customers/", json=data)
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/customers/all/")
async def get_all_customers():
    response = requests.get(f"{CUSTOMER_SERVICE_URL}/customers/all/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.post("/api/users/login/")
async def login_user(data: dict):
    response = requests.post(f"{CUSTOMER_SERVICE_URL}/users/login/", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Item_Service
@app.post("/api/books/")
async def create_book(data: dict):
    response = requests.post(f"{ITEM_SERVICE_URL}/books/", json=data)
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/books/all/")
async def get_all_books():
    response = requests.get(f"{ITEM_SERVICE_URL}/books/all/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/books/{itemId}/")
async def get_book_detail(itemId: str):
    response = requests.get(f"{ITEM_SERVICE_URL}/books/{itemId}/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.put("/api/books/{itemId}/update/")
async def update_book(itemId: str, data: dict):
    response = requests.put(f"{ITEM_SERVICE_URL}/books/{itemId}/update/", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.delete("/api/books/{itemId}/delete/")
async def delete_book(itemId: str):
    response = requests.delete(f"{ITEM_SERVICE_URL}/books/{itemId}/delete/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.post("/api/laptops/")
async def create_laptop(data: dict):
    response = requests.post(f"{ITEM_SERVICE_URL}/laptops/", json=data)
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/laptops/all/")
async def get_all_laptops():
    response = requests.get(f"{ITEM_SERVICE_URL}/laptops/all/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/laptops/{itemId}/")
async def get_laptop_detail(itemId: str):
    response = requests.get(f"{ITEM_SERVICE_URL}/laptops/{itemId}/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.put("/api/laptops/{itemId}/update/")
async def update_laptop(itemId: str, data: dict):
    response = requests.put(f"{ITEM_SERVICE_URL}/laptops/{itemId}/update/", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.delete("/api/laptops/{itemId}/delete/")
async def delete_laptop(itemId: str):
    response = requests.delete(f"{ITEM_SERVICE_URL}/laptops/{itemId}/delete/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.post("/api/phones/")
async def create_phone(data: dict):
    response = requests.post(f"{ITEM_SERVICE_URL}/phones/", json=data)
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/phones/all/")
async def get_all_phones():
    response = requests.get(f"{ITEM_SERVICE_URL}/phones/all/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/phones/{itemId}/")
async def get_phone_detail(itemId: str):
    response = requests.get(f"{ITEM_SERVICE_URL}/phones/{itemId}/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.put("/api/phones/{itemId}/update/")
async def update_phone(itemId: str, data: dict):
    response = requests.put(f"{ITEM_SERVICE_URL}/phones/{itemId}/update/", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.delete("/api/phones/{itemId}/delete/")
async def delete_phone(itemId: str):
    response = requests.delete(f"{ITEM_SERVICE_URL}/phones/{itemId}/delete/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/items/all/")
async def get_all_items():
    response = requests.get(f"{ITEM_SERVICE_URL}/items/all/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Comment APIs (Item_Service)
@app.post("/api/comments/")
async def create_comment(data: dict):
    response = requests.post(f"{ITEM_SERVICE_URL}/comments/", json=data)
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/comments/item/{itemId}/")
async def get_comments_by_item(itemId: str):
    response = requests.get(f"{ITEM_SERVICE_URL}/comments/item/{itemId}/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/comments/all/")
async def get_all_comments():
    response = requests.get(f"{ITEM_SERVICE_URL}/comments/all/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Cart_Service
@app.post("/api/carts/")
async def create_cart(data: dict):
    response = requests.post(f"{CART_SERVICE_URL}/carts/", json=data)
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.post("/api/carts/{cartId}/add-item/")
async def add_item_to_cart(cartId: str, data: dict):
    response = requests.post(f"{CART_SERVICE_URL}/carts/{cartId}/add-item/", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.delete("/api/carts/{cartId}/remove-item/{itemId}/")
async def remove_item_from_cart(cartId: str, itemId: str):
    response = requests.delete(f"{CART_SERVICE_URL}/carts/{cartId}/{itemId}/remove/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.put("/api/carts/{cartId}/update-quantity/{itemId}/")
async def update_item_quantity(cartId: str, itemId: str, data: dict):
    response = requests.put(f"{CART_SERVICE_URL}/carts/{cartId}/{itemId}/update-quantity/", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/carts/{cartId}/items/")
async def get_all_items_in_cart(cartId: str):
    response = requests.get(f"{CART_SERVICE_URL}/carts/{cartId}/items/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/carts/customer/{customerId}/")
async def get_cart_by_customer(customerId: str):
    response = requests.get(f"{CART_SERVICE_URL}/carts/customer/{customerId}/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Payment_Service
@app.post("/api/payments/")
async def create_payment(data: dict):
    response = requests.post(f"{PAYMENT_SERVICE_URL}/payments/", json=data)
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/payments/all/")
async def get_all_payments():
    response = requests.get(f"{PAYMENT_SERVICE_URL}/payments/all/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/payments/{paymentId}/")
async def get_payment_detail(paymentId: str):
    response = requests.get(f"{PAYMENT_SERVICE_URL}/payments/{paymentId}/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.put("/api/payments/{paymentId}/update/")
async def update_payment(paymentId: str, data: dict):
    response = requests.put(f"{PAYMENT_SERVICE_URL}/payments/{paymentId}/update/", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.delete("/api/payments/{paymentId}/delete/")
async def delete_payment(paymentId: str):
    response = requests.delete(f"{PAYMENT_SERVICE_URL}/payments/{paymentId}/delete/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Shipment_Service
@app.post("/api/shipments/")
async def create_shipment(data: dict):
    response = requests.post(f"{SHIPMENT_SERVICE_URL}/shipments/", json=data)
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/shipments/all/")
async def get_all_shipments():
    response = requests.get(f"{SHIPMENT_SERVICE_URL}/shipments/all/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/shipments/{shipmentId}/")
async def get_shipment_detail(shipmentId: str):
    response = requests.get(f"{SHIPMENT_SERVICE_URL}/shipments/{shipmentId}/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.put("/api/shipments/{shipmentId}/update/")
async def update_shipment(shipmentId: str, data: dict):
    response = requests.put(f"{SHIPMENT_SERVICE_URL}/shipments/{shipmentId}/update/", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.delete("/api/shipments/{shipmentId}/delete/")
async def delete_shipment(shipmentId: str):
    response = requests.delete(f"{SHIPMENT_SERVICE_URL}/shipments/{shipmentId}/delete/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Order_Service
@app.post("/api/orders/")
async def create_order(data: dict):
    response = requests.post(f"{ORDER_SERVICE_URL}/orders/", json=data)
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/orders/all/")
async def get_all_orders():
    response = requests.get(f"{ORDER_SERVICE_URL}/orders/all/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/orders/{orderId}/")
async def get_order_detail(orderId: str):
    response = requests.get(f"{ORDER_SERVICE_URL}/orders/{orderId}/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.put("/api/orders/{orderId}/update/")
async def update_order(orderId: str, data: dict):
    response = requests.put(f"{ORDER_SERVICE_URL}/orders/{orderId}/update/", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.delete("/api/orders/{orderId}/delete/")
async def delete_order(orderId: str):
    response = requests.delete(f"{ORDER_SERVICE_URL}/orders/{orderId}/delete/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Admin_Service
@app.post("/api/admins/")
async def create_admin(data: dict):
    response = requests.post(f"{ADMIN_SERVICE_URL}/admins/", json=data)
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/admins/all/")
async def get_all_admins():
    response = requests.get(f"{ADMIN_SERVICE_URL}/admins/all/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/admins/{adminId}/")
async def get_admin_detail(adminId: str):
    response = requests.get(f"{ADMIN_SERVICE_URL}/admins/{adminId}/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.put("/api/admins/{adminId}/update/")
async def update_admin(adminId: str, data: dict):
    response = requests.put(f"{ADMIN_SERVICE_URL}/admins/{adminId}/update/", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.delete("/api/admins/{adminId}/delete/")
async def delete_admin(adminId: str):
    response = requests.delete(f"{ADMIN_SERVICE_URL}/admins/{adminId}/delete/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.get("/api/comments/classify/{commentId}/")
async def classify_comment(commentId: str):
    response = requests.get(f"{ITEM_SERVICE_URL}/comments/classify/{commentId}/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)