from fastapi import FastAPI, UploadFile, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="../app/templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_file(file: UploadFile):
    contents = await file.read()
    print("файл загружен")
    # Здесь выполняются операции с файлом (в нашем случае предсказание плотности)
    return {"message": "Файл успешно загружен."}