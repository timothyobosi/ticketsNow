#import FirstAPI class from the fastapi to create the web instance
from fastapi import FastAPI
#import tthe custom routes.py where endpoints live
from customer_service import routes

#create the FastAPI application instance(gives it title + version)
app = FastAPI(title="Customer Service", version="1.0.0")

#Register the router with the app
#attach all customer-related routes under /customers path
#and tag them with "Customer APIs"
app.include_router(routes.router, prefix="/customers", tags=["Customer APIs"])

#Define the root endpoint
@app.get("/")
async def root():
    return{"message": "Customer service is live"}