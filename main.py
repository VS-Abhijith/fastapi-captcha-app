from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import io
import re

app = FastAPI()

@app.post("/captcha")
async def solve_captcha(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    extracted_text = pytesseract.image_to_string(image)

    match = re.search(r"(\d{8})\s*\*?\s*(\d{8})", extracted_text)
    if not match:
        return JSONResponse(
            content={"error": "Could not parse numbers from image"},
            status_code=400
        )

    num1 = int(match.group(1))
    num2 = int(match.group(2))
    result = num1 * num2

    return {
        "answer": result,
        "email": "22ds3000188@ds.study.iitm.ac.in"
    }
