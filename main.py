from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Products(BaseModel):
    id: int
    productname: str
    description: str
    brand: str
    categories: str
    count: int
    price: int

class Basket(BaseModel):
    id: int
    products: str
    count: int

class Staff(BaseModel):
    id: int
    firstname: str
    lastname: str

class Customer(BaseModel):
    id: int
    firstname: str
    lastname: str

class CustomerHasBasket(BaseModel):
    id: int
    products: str
    customer: str

class Order(BaseModel):
    id: int
    customerhasbasket: str
    staff:  str
    createAt: int
    overall: int

mall_db = []

@app.post("/products/", response_model=Products)
def create_mall_item(products: Products):
    mall_db.append(products)
    return products

@app.post("/basket/", response_model=Basket)
def create_mall_item(basket: Basket):
    mall_db.append(basket)
    return basket

@app.post("/staff/", response_model=Staff)
def create_mall_item(staff: Staff):
    mall_db.append(Staff)
    return staff

@app.post("/customer/", response_model=Customer)
def create_mall_item(customer: Customer):
    mall_db.append(customer)
    return customer

@app.post("/customerhasbasket/", response_model=CustomerHasBasket)
def create_mall_item(customerhasbasket: CustomerHasBasket):
    mall_db.append(customerhasbasket)
    return customerhasbasket

@app.post("/order/", response_model=Order)
def create_mall_item(order: Order):
    mall_db.append(order)
    return order

#

@app.get("/products/", response_model=List[Products])
def read_mall_items():
    return mall_db

@app.get("/basket/", response_model=List[Basket])
def read_mall_items():
    return mall_db

@app.get("/staff/", response_model=List[Staff])
def read_mall_items():
    return mall_db

@app.get("/customer/", response_model=List[Customer])
def read_mall_items():
    return mall_db

@app.get("/customerhasbasket/", response_model=List[CustomerHasBasket])
def read_mall_items():
    return mall_db

@app.get("/order/", response_model=List[Order])
def read_mall_items():
    return mall_db

#

@app.get("/products/{products_id}", response_model=Products)
def read_mall_item(products_id: int):
    for products in mall_db:
        if products.id == products_id:
            return products
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/basket/{basket_id}", response_model=Basket)
def read_mall_item(basket_id: int):
    for basket in mall_db:
        if basket.id == basket_id:
            return basket
    raise HTTPException(status_code=404, detail="Basket not found")

@app.get("/staff/{staff_id}", response_model=Staff)
def read_mall_item(staff_id: int):
    for staff in mall_db:
        if staff.id == staff_id:
            return staff
    raise HTTPException(status_code=404, detail="Staff not found")

@app.get("/customer/{customer_id}", response_model=Customer)
def read_mall_item(customer_id: int):
    for customer in mall_db:
        if customer.id == customer_id:
            return customer
    raise HTTPException(status_code=404, detail="Customer not found")

@app.get("/customerhasbasket/{customerhasbasket_id}", response_model=CustomerHasBasket)
def read_mall_item(customerhasbasket_id: int):
    for customerhasbasket in mall_db:
        if customerhasbasket.id == customerhasbasket_id:
            return customerhasbasket
    raise HTTPException(status_code=404, detail="Customer's basket not found")

@app.get("/order/{order_id}", response_model=Order)
def read_mall_item(order_id: int):
    for order in mall_db:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

# put

@app.put("/products/{products_id}", response_model=Products)
def update_mall_item(products_id: int, products: Products):
    for index, existing_products in enumerate(mall_db):
        if existing_products.id == products_id:
            mall_db[index] = products
            return products
    raise HTTPException(status_code=404, detail="Product ID not found")

@app.put("/basket/{basket_id}", response_model=Basket)
def update_mall_item(basket_id: int, basket: Basket):
    for index, existing_basket in enumerate(mall_db):
        if existing_basket.id == basket_id:
            mall_db[index] = basket
            return basket
    raise HTTPException(status_code=404, detail="Basket ID not found")

@app.put("/staff/{staff_id}", response_model=Staff)
def update_mall_item(staff_id: int, staff: Staff):
    for index, existing_staff in enumerate(mall_db):
        if existing_staff.id == staff_id:
            mall_db[index] = staff
            return staff
    raise HTTPException(status_code=404, detail="Staff ID not found")

@app.put("/customer/{customer_id}", response_model=Customer)
def update_mall_item(customer_id: int, customer: Customer):
    for index, existing_customer in enumerate(mall_db):
        if existing_customer.id == customer_id:
            mall_db[index] = customer
            return customer
    raise HTTPException(status_code=404, detail="Customer ID not found")

@app.put("/customerhasbasket/{customerhasbasket_id}", response_model=CustomerHasBasket)
def update_mall_item(customerhasbasket_id: int, customerhasbasket: CustomerHasBasket):
    for index, existing_customerhasbasket in enumerate(mall_db):
        if existing_customerhasbasket.id == customerhasbasket_id:
            mall_db[index] = customerhasbasket
            return customerhasbasket
    raise HTTPException(status_code=404, detail="Customer's basket ID not found")

@app.put("/order/{order_id}", response_model=Order)
def update_mall_item(order_id: int, order: Order):
    for index, existing_order in enumerate(mall_db):
        if existing_order.id == order_id:
            mall_db[index] = order
            return order
    raise HTTPException(status_code=404, detail="Order ID not found")


# delete

@app.delete("/products/{products_id}", response_model=Products)
def delete_mall_item(products_id: int):
    for index, products in enumerate(mall_db):
        if products.id == products_id:
            deleted_products = mall_db.pop(index)
            return deleted_products
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/basket/{basket_id}", response_model=Basket)
def delete_mall_item(basket_id: int):
    for index, basket in enumerate(mall_db):
        if basket.id == basket_id:
            deleted_basket = mall_db.pop(index)
            return deleted_basket
    raise HTTPException(status_code=404, detail="Basket not found")

@app.delete("/staff/{staff_id}", response_model=Staff)
def delete_mall_item(staff_id: int):
    for index, staff in enumerate(mall_db):
        if staff.id == staff_id:
            deleted_staff = mall_db.pop(index)
            return deleted_staff
    raise HTTPException(status_code=404, detail="Staff not found")

@app.delete("/customer/{customer_id}", response_model=Customer)
def delete_mall_item(customer_id: int):
    for index, customer in enumerate(mall_db):
        if customer.id == customer_id:
            deleted_customer = mall_db.pop(index)
            return deleted_customer
    raise HTTPException(status_code=404, detail="Customer not found")

@app.delete("/customerhasbasket/{customerhasbasket_id}", response_model=CustomerHasBasket)
def delete_mall_item(customerhasbasket_id: int):
    for index, customerhasbasket in enumerate(mall_db):
        if customerhasbasket.id == customerhasbasket_id:
            deleted_customerhasbasket = mall_db.pop(index)
            return deleted_customerhasbasket
    raise HTTPException(status_code=404, detail="Customer's basket not found")

@app.delete("/order/{order_id}", response_model=Order)
def delete_mall_item(order_id: int):
    for index, order in enumerate(mall_db):
        if order.id == order_id:
            deleted_order = mall_db.pop(index)
            return deleted_order
    raise HTTPException(status_code=404, detail="Order not found")
