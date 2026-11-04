"""Loads the pickled Random Forest once and turns a soil/weather reading into advice."""
import pickle
from pathlib import Path
import numpy as np

MODEL_PATH = Path(__file__).parent / "ml" / "Crop_recommender_Rf.pkl"
_bundle = None

def _load():
    global _bundle
    if _bundle is None:
        with open(MODEL_PATH, "rb") as f:   # only load pickle files you created yourself
            _bundle = pickle.load(f)
    return _bundle

def predict(values, top=3):
    """values: dict with the model's feature columns. Returns [(crop, probability), ...]."""
    b = _load(); model = b["model"]; cols = b["feature_cols"]
    row = [[float(values[c]) for c in cols]]
    if hasattr(model, "feature_names_in_"):
        import pandas as pd
        X = pd.DataFrame(row, columns=cols)
    else:
        X = np.array(row)
    proba = model.predict_proba(X)[0]
    order = np.argsort(proba)[::-1][:top]
    return [(str(model.classes_[i]), float(proba[i])) for i in order]

def soil_notes(v):
    """Plain-language checks on the readings. Rules of thumb, not a substitute for a soil test."""
    n = []
    if v["ph"] < 5.5: n.append(("warn", "Soil is acidic (pH below 5.5). Liming with agricultural lime can raise pH."))
    elif v["ph"] > 7.8: n.append(("warn", "Soil is alkaline (pH above 7.8). Gypsum and compost help bring it down."))
    else: n.append(("ok", "Soil pH is in a comfortable range for most crops."))
    if v["N"] < 40: n.append(("warn", "Nitrogen is low. Compost, green manure or split doses of urea can help."))
    if v["N"] > 100: n.append(("info", "Nitrogen is high. Skip extra urea this season to avoid weak, leafy growth."))
    if v["P"] < 30: n.append(("warn", "Phosphorus is low. Single super phosphate or DAP at sowing can help."))
    if v["K"] < 30: n.append(("warn", "Potassium is low. Muriate of potash or wood ash can help."))
    if v["rainfall"] < 60: n.append(("info", "Rainfall is low. Plan irrigation and consider mulching to hold moisture."))
    if v["rainfall"] > 250: n.append(("info", "Rainfall is very high. Make sure drainage channels are clear."))
    if v["humidity"] > 85: n.append(("info", "Humidity is high. Watch for fungal disease and keep good spacing between plants."))
    if v["temperature"] > 35: n.append(("info", "Heat stress is likely. Irrigate in the evening and mulch the soil."))
    return n
