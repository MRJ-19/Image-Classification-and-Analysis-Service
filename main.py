from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.concurrency import run_in_threadpool
from .model_service import analyze_and_predict
from app.schemas import PredictionResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(
    title="Image Classification Service",
    description="MobileNetV2 based image analysis API",
    version="1.0.0"
)

@app.post("/predict", response_model=PredictionResponse)
async def predict_image(file: UploadFile = File(...)):
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File provided is not an image.")

    contents = await file.read()
    
    try:
        # Offload CPU-bound ML task to a separate thread
        results = await run_in_threadpool(analyze_and_predict, contents)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference failed: {str(e)}")

    return {
        "filename": file.filename,
        "analysis": results["analysis"],
        "predictions": results["predictions"],
        "status": "success"
    }
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')