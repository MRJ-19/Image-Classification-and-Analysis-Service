from pydantic import BaseModel
from typing import List

class AnalysisMetadata(BaseModel):
    format: str
    mode: str
    size: List[int]

class PredictionResult(BaseModel):
    label: str
    score: float

class PredictionResponse(BaseModel):
    filename: str
    analysis: AnalysisMetadata
    predictions: List[PredictionResult]
    status: str