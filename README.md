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

## Supported Features
✅ Auto feature & disease detection

✅ Real-time multi-disease prediction

✅ Dropdowns for categorical input (Gender, Smoking, etc.)

✅ Instant confidence scoring (risk: LOW / HIGH)

✅ Handles messy/partial data with preprocessing

✅ Responsive UI - no HTML files needed

 ## 🛠️Tech Stack

| Tool          | Role                 |
| ------------- | -------------------- |
| Python        | Core programming     |
| Flask         | Web framework        |
| Pandas, NumPy | Data handling        |
| Scikit-learn  | ML utilities         |
| XGBoost       | Model backend        |
| joblib        | Model saving/loading |


## 📈 Example Usage

Detect risks for Diabetes, Heart Disease, COPD, Tuberculosis, Migraine, Hepatitis, etc.


Just fill in age, BMI, symptoms, and medical history—get predictions instantly.

## 📌 Notes

*Make sure your dataset contains meaningful numeric + categorical data for features, and binary values for target disease columns.


*You can customize the form fields in app.py → feature_list.

## 🏁 Ready to Use in Under 3 Minutes!

1)Clone

2)Install

3)Add dataset

4)Run: python run.py

5)Predict!

```bash
# Clone the repo
git clone https://github.com/mandrita16/MultipleDiseasePrediction.git
cd MultipleDiseasePrediction

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate   # Windows
# OR
source venv/bin/activate # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
```

## ⚠️ Troubleshooting

🛑 Prediction not working?

Ensure your dataset has all required feature columns and no string/invalid data in numeric fields.

🛑 Decimal age or negative values?

Use whole numbers for Age, and only use decimals for features like BMI or Sugar Level.

🛑 400 Bad Request?

This usually means there's a mismatch between form input names and trained model features.


Kindly give a star 

Made with ❤️ by Mandrita Dasgupta
