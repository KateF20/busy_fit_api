from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "YOU ARE AN IDIOT!!!"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Helloooooooooooo {name.title()}"}
