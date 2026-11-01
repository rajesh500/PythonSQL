from fastapi import FastAPI, HTTPException

app = FastAPI(title="Simple Customer API")

customers = {
    101: {
        "customer_id": 101,
        "name": "Rajesh",
        "city": "Chicago"
    },
    102: {
        "customer_id": 102,
        "name": "Priya",
        "city": "Dallas"
    }
}


@app.get("/")
def home():
    return {"message": "My Python API is running!"}


@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    customer = customers.get(customer_id)

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer
