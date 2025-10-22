import os
import io
import base64
from typing import Optional, Any, Dict

from flask import Flask, request, jsonify
from ultralytics import YOLO
from PIL import Image
import numpy as np

# Configuration
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MODEL_PATH = os.getenv(
    "MODEL_PATH",
    os.path.join(PROJECT_ROOT, "runs", "rust_train", "weights", "best.pt")
)

app = Flask(__name__)

_model: Optional[YOLO] = None


def get_model() -> YOLO:
    global _model
    if _model is None:
        if not os.path.exists(DEFAULT_MODEL_PATH):
            raise FileNotFoundError(
                f"Model weights not found at '{DEFAULT_MODEL_PATH}'. Set MODEL_PATH env var to override."
            )
        _model = YOLO(DEFAULT_MODEL_PATH)
    return _model


@app.get("/health")
def health() -> Any:
    try:
        m = get_model()
        return jsonify({
            "status": "ok",
            "model_path": DEFAULT_MODEL_PATH,
            "classes": getattr(m, "names", {}),
        })
    except Exception as e:
        return jsonify({"status": "error", "error": str(e), "model_path": DEFAULT_MODEL_PATH}), 500


def read_image_from_request() -> Image.Image:
    # Multipart: form-data 'file'
    if "file" in request.files:
        fs = request.files["file"]
        return Image.open(fs.stream).convert("RGB")
    # Raw bytes
    if request.data:
        return Image.open(io.BytesIO(request.data)).convert("RGB")
    raise ValueError("No image provided. Send multipart/form-data 'file' or raw image bytes in body.")


def results_to_payload(res) -> Dict[str, Any]:
    boxes = []
    names = res.names or {}
    if getattr(res, "boxes", None) is not None:
        xyxy = res.boxes.xyxy.cpu().numpy()
        conf = res.boxes.conf.cpu().numpy()
        cls = res.boxes.cls.cpu().numpy()
        for i in range(len(xyxy)):
            x1, y1, x2, y2 = xyxy[i].tolist()
            boxes.append({
                "box": [x1, y1, x2, y2],
                "confidence": float(conf[i]),
                "class_id": int(cls[i]),
                "class_name": names.get(int(cls[i]), str(int(cls[i])))
            })
    return {
        "boxes": boxes,
        "names": names,
        "orig_shape": getattr(res, "orig_shape", None),
        "path": getattr(res, "path", None)
    }


def encode_result_image(res) -> str:
    arr = res.plot()  # BGR numpy array
    if arr.ndim == 3 and arr.shape[2] == 3:
        arr = arr[:, :, ::-1]  # to RGB
    img = Image.fromarray(arr)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=90)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")


@app.post("/predict")
def predict() -> Any:
    conf = float(request.args.get("conf", request.form.get("conf", 0.25)))
    imgsz = int(request.args.get("imgsz", request.form.get("imgsz", 640)))
    iou = float(request.args.get("iou", request.form.get("iou", 0.7)))
    return_image = str(request.args.get("return_image", request.form.get("return_image", "false"))).lower() in {"1", "true", "yes"}

    try:
        img = read_image_from_request()
        model = get_model()
        results = model.predict(source=img, conf=conf, imgsz=imgsz, iou=iou, verbose=False)
        if not results:
            return jsonify({"error": "No results returned by model"}), 500
        res = results[0]
        # Save annotated result image into Uploads as *_pred.jpg
        basePath = os.path.dirname(__file__)
        upload_dir = os.path.join(basePath, 'Uploads')
        os.makedirs(upload_dir, exist_ok=True)
        # derive a base name from result path if available
        base_name = os.path.splitext(os.path.basename(getattr(res, 'path', '') or 'predict'))[0]
        pred_name = f"{base_name}_pred.jpg"
        pred_path = os.path.join(upload_dir, pred_name)
        arr = res.plot()

        Image.fromarray(arr).save(pred_path, format="JPEG", quality=90)

        payload = results_to_payload(res)
        payload["pred_image_path"] = pred_path
        if return_image:
            payload["image_base64"] = encode_result_image(res)
        return jsonify(payload)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
