# ♻️ EcoSort AI

## AI-Powered Smart Waste Classification and Sustainability Assistant

EcoSort AI is an intelligent waste classification application that uses Artificial Intelligence to identify objects from images and provide waste disposal recommendations.

The application helps users understand how an item should be disposed of and promotes responsible consumption and sustainable waste management.

---

## 🚀 Live Demo

[🌐 Open EcoSort AI](https://ecosort-ai-shriya.streamlit.app)

---


## 🌟 Features

- 🤖 AI-powered object detection
- 🖼️ Image upload and analysis
- 🔍 YOLO-based object detection
- 🧠 Vision Transformer fallback for object classification
- ♻️ Waste category recommendations
- 🗑️ Disposal guidance
- 🌱 Sustainability impact information
- 🎯 AI confidence score
- 🌍 SDG 12 awareness
- 💻 User-friendly application interface
- 🚀 One-click launcher for Windows

---

## 🧠 How EcoSort AI Works

1. User uploads an image.
2. YOLO AI attempts to detect the object.
3. If YOLO cannot identify the object, Vision Transformer AI is used as a fallback.
4. The detected object is analyzed.
5. EcoSort AI provides:
   - Object name
   - AI confidence
   - Waste category
   - Disposal recommendation
   - Sustainability information

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Ultralytics YOLO
- Vision Transformer
- Hugging Face Transformers
- PyTorch
- OpenCV
- Pillow
- Pandas

---

## 📁 Project Structure

```text
EcoSortAI/
│
├── assets/
│   └── test_images/
│       └── test.jpg.png
│
├── src/
│   ├── __init__.py
│   ├── classifier.py
│   ├── recommendations.py
│   └── sustainability.py
│
├── tests/
│   ├── __init__.py
│   └── test_classifier.py
│
├── app.py
├── Start_EcoSort.bat
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd EcoSortAI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Application

```bash
python -m streamlit run app.py
```

Then open the local URL displayed in your browser.

---

## 🖱️ One-Click Launcher

Windows users can double-click:

```text
Start_EcoSort.bat
```

---

## 🌍 Sustainability Goal

### SDG 12 — Responsible Consumption and Production

EcoSort AI encourages proper waste segregation and responsible disposal decisions.

---

## 🔮 Future Improvements

- 📷 Live camera waste detection
- 📱 Mobile application
- 📊 Scan history
- 🌍 Personal Eco Impact Dashboard
- 🏆 EcoScore system
- 🗑️ More detailed waste categories
- 📍 Location-based recycling recommendations

---

## 👩‍💻 Developer

**Shriya Mishra**

Computer Science Engineering Student

---

# ♻️ EcoSort AI

**AI for Smarter Waste Management and Sustainable Communities**
