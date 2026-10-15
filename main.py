
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.get("/api/table/{number}")
async def generate_table(number: int, limit: int = 10):
    table = []

    for i in range(1, limit + 1):
        table.append({
            "multiplier": i,
            "result": number * i
        })

    return {
        "number": number,
        "table": table
    }
