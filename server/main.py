from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"data": {
        "first_name": "Joko",
        "last_name": "Saputro"
    }}

@app.get("/about")
def about():
    return {"data": "about page"}

def main():
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()