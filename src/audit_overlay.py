import cv2

def create_overlay(img, detected_answers, score, save_path):
    overlay = img.copy()
    cv2.putText(overlay, f"Score: {score}", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    cv2.imwrite(save_path, overlay)
