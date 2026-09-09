from ultralytics import YOLO
from transformers import pipeline


class WasteClassifier:

    def __init__(self):

        # Primary AI: YOLO object detection
        self.model = YOLO("yolov8n.pt")

        # Fallback AI: General image classification
        print("Loading image classification AI...")

        self.image_classifier = pipeline(
            "image-classification",
            model="google/vit-base-patch16-224"
        )


    def classify(self, image_path):

        # First try YOLO
        results = self.model(image_path)

        detected_objects = []

        for result in results:
            for box in result.boxes:

                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                object_name = self.model.names[class_id]

                detected_objects.append({
                    "object": object_name,
                    "confidence": round(confidence * 100, 2),
                    "source": "YOLO"
                })

        # If YOLO detects something, return it
        if detected_objects:
            return detected_objects

        # Fallback to image classification
        print("YOLO found no object. Using fallback AI...")

        predictions = self.image_classifier(image_path)

        if predictions:

            best_prediction = predictions[0]

            return [{
                "object": best_prediction["label"],
                "confidence": round(best_prediction["score"] * 100, 2),
                "source": "Vision Transformer"
            }]

        # Final fallback
        return [{
            "object": "unknown",
            "confidence": 0.0,
            "source": "No confident prediction"
        }]