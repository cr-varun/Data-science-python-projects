Rust Corrosion Detection - Quick Start and Repro Steps

1) Use the project virtual environment (venv)
- Confirm the Notebook or terminal is using this interpreter:
  python -c "import sys; print(sys.executable)"
  Expect: ...\Rust_corrosion\.venv\Scripts\python.exe

2) Upgrade pip in this venv
  python -m pip install --upgrade pip

3) Install PyTorch with CUDA 12.4 runtime in this venv
  python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

4) Install Ultralytics YOLO and Pillow
  python -m pip install ultralytics pillow

5) Verify Torch + CUDA
  python -c "import torch; print('torch:', torch.__version__, 'cuda:', torch.version.cuda); \
  print('CUDA available:', torch.cuda.is_available()); \
  print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'No CUDA GPU detected')"
  Expected: CUDA version shown (e.g., 12.4) and CUDA available: True

6) Run the Flask inference API
- File: rust_api.py
- Default model path: runs/rust_train/weights/best.pt
- To override: set env var MODEL_PATH to your weights file
  PowerShell example:
    $env:MODEL_PATH = "C:\Users\varun\Desktop\DATA SCIENCE\Data Science_new\Projects\Rust_corrosion\runs\rust_train\weights\best.pt"
- Start server:
  python rust_api.py

7) Test endpoints
- Health
  Invoke-RestMethod -Method GET http://localhost:5000/health

- Predict with multipart image
  Invoke-RestMethod -Uri "http://localhost:5000/predict?conf=0.25&imgsz=640" -Method POST -Form @{ file = Get-Item "C:\path\to\image.jpg" }

- Predict with raw bytes
  $bytes = [System.IO.File]::ReadAllBytes("C:\path\to\image.jpg")
  Invoke-RestMethod -Uri "http://localhost:5000/predict?return_image=true" -Method POST -Body $bytes -ContentType "application/octet-stream"

Notes
- Jupyter: If the notebook shows CPU-only Torch, switch the kernel to the project venv or install CUDA wheels inside the current kernel using sys.executable and subprocess.
- Training: The notebook Model_train_v1.ipynb was used to train and validate; best weights saved under runs/rust_train/weights/best.pt.
