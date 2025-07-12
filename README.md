# ⚡ Multi-Disease Prediction System

A lightning-fast, intelligent system that predicts **multiple health risks** in real-time based on patient input using a powerful **XGBoost + MultiOutputClassifier** ML model. Built with Flask, scikit-learn, and a sleek UI, this system is ideal for hackathons, demos, or medical prototypes.

---

## 📂 Project Structure



---

## 🚀 Setup & Run in VS Code

### 🧱 Prerequisites

- Python 3.10+ (install from [python.org](https://www.python.org/downloads/))
- Git
- VS Code (recommended)
- Basic terminal/command-line knowledge

---

### 🧪 Step-by-Step Setup

🧭 **1. Clone this repository**
```bash
git clone https://github.com/mandrita16/MultipleDiseasePrediction.git
cd MultipleDiseasePrediction
```

🔒 **2. Create a virtual environment**
```bash
python -m venv venv
```

🟢 **3. Activate the environment**

On Windows (PowerShell):

```bash
.\venv\Scripts\Activate
```

📦 **4. Install the required packages**

```bash
pip install -r requirements.txt
```

📄 **5. Add your dataset**

```bash
# Paste your cleaned dataset into the /data folder
# Name it exactly: disease_dataset.csv
```

🚀 **6. Launch the app**

```bash
python run.py
```


## 🌐 Access the Web Interface

  Once the app is running, open your browser and go to:
```bash
http://localhost:5000
```
You'll see a beautiful and responsive form where you can enter patient details to get disease predictions.







