from fastapi import FastAPI, Query
from omrr.preprocessing import preprocess_image
from omrr.detection import detect_bubbles
from omrr.evaluation import evaluate_sheet
from pathlib import Path
import pandas as pd
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}
app = FastAPI(title="OMR Evaluation System")

DATA_DIR = Path("./data").resolve()  # Change path if using Docker

@app.post("/process-set/")
async def process_set(set_name: str = Query(..., description="Name of the OMR set")):
    folder = DATA_DIR / set_name
    if not folder.exists():
        return {"error": f"Set '{set_name}' not found"}

    try:
        df = pd.read_excel(DATA_DIR / "ans_key.xlsx")
    except FileNotFoundError:
        return {"error": "Answer key file not found"}

    if set_name not in df.columns:
        return {"error": f"Set {set_name} not in answer key"}

    results = []
    for img_file in folder.glob("*.png"):  # adjust extension
        img = preprocess_image(str(img_file))
        bubbles = detect_bubbles(img)
        score_data = evaluate_sheet(bubbles, df[set_name].tolist())
        results.append({"file": img_file.name, "score": score_data["score"], "answers": score_data["answers"]})

    return {"set": set_name, "results": results}
