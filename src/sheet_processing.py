import cv2
import os
import json
from .preprocessing import preprocess
from .sheet_detection import detect_sheet
from .grid_mapper import map_grid
from .bubble_scoring import detect_answers

# --- Paths ---
data_dir = os.path.join(os.getcwd(), "data")
templates_dir = os.path.join(os.getcwd(), "templates")
storage_dir = os.path.join(os.getcwd(), "storage")

sheet_path = os.path.join(data_dir, "omr3.png")
template_path = os.path.join(templates_dir, "template_setA.json")
key_path = os.path.join(templates_dir, "answer_key_setA.json")
output_path = os.path.join(storage_dir, "scored_omr1.png")

# --- Load OMR image ---
image = cv2.imread(sheet_path)
if image is None:
    raise FileNotFoundError(f"Cannot load image: {sheet_path}")

# --- Preprocess ---
processed = preprocess(image)

# --- Detect sheet ---
sheet = detect_sheet(processed)

# --- Map bubbles to grid ---
grid = map_grid(sheet, num_questions=10, num_options=4)

# --- Detect filled bubbles ---
answers = detect_answers(sheet, grid)

# --- Save detected answers ---
with open(template_path, "w") as f:
    json.dump(answers, f, indent=4)

print("Detected answers:", answers)

# --- Load answer key ---
with open(key_path) as f:
    key = json.load(f)

# --- Fix key type mismatch: convert answers keys to strings ---
answers_str_keys = {str(k): v for k, v in answers.items()}

# --- Calculate score ---
score = sum(answers_str_keys.get(q) == a for q, a in key.items())
total_questions = len(key)
percentage = (score / total_questions) * 100

print(f"Score: {score}/{total_questions}")
print(f"Percentage: {percentage:.2f}%")

# --- Optional: Save overlay (if audit_overlay.py exists) ---
# from .audit_overlay import save_overlay
# save_overlay(sheet, grid, answers, output_path)
