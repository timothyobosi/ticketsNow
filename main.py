#import FirstAPI class from the fastapi
from fastapi import FastAPI

#create the FastAPI application instance
app = FastAPI

#App startup event(runs when the app starts)
@app.on_event("startup")
async def startup(): #decorator tells FastAPI to run this function during startup
	pass

#App shutdown event(run when the app stops)
@app.on_event("shutdown")
async def shutdown(): #asynchronous function used to handle clean up tasks when your FasAPI is shutting down
	pass

#Routers

#Root route to confirm the app is running
@app.get("/") #Route decorator- Tells FasAPI to call func below when the client sends a GET request to the root URL(/)
async def read_root(): #Asynchronous function FastAPI will invoke when someone visits /
	return{"message","Welcome to my API"} #Returns JSON response, FastAPI converts Python dictionaries into JSON for HTTP responses
