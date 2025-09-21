import cv2

def detect_answers(sheet_image, grid):
    # Convert to grayscale if needed
    if len(sheet_image.shape) == 3 and sheet_image.shape[2] == 3:
        gray = cv2.cvtColor(sheet_image, cv2.COLOR_BGR2GRAY)
    else:
        gray = sheet_image  # already grayscale

    # Adaptive threshold for robustness
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV, 25, 10
    )

    answers = {}
    for q, options in grid.items():
        detected = None
        for idx, (x, y, w, h) in enumerate(options):
            bubble = thresh[y:y+h, x:x+w]
            filled = cv2.countNonZero(bubble)
            if filled > 100:  # Lower if not detecting
                detected = chr(65 + idx)  # A, B, C, D
        if detected:
            answers[q] = detected

    return answers
