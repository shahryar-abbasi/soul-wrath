from fastapi import FastAPI

# this instance allows me to create routes.
app = FastAPI()  # fastapi instance

# localhost:8000/
@app.get("/")  # root/home
def root():
    return {"message": "Welcome to FastAPI...!"}

@app.get("/greet")
def greet():
    return {"message": "Hello All."}

# path parameter
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name.title()}"}


#python -m uvicorn main:app --reload
#uv run fastapi dev main.py