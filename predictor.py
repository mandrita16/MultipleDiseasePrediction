import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import accuracy_score, classification_report
import xgboost as xgb
import joblib
import os

class UltraPredictor:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.feature_cols = []
        self.target_cols = []
        
    def auto_detect_columns(self, df):
        """Auto-detect feature and target columns"""
        # Common disease keywords
        disease_keywords = ['diabetes', 'heart', 'hypertension', 'stroke', 'cancer', 
                           'kidney', 'liver', 'asthma', 'disease', 'condition']
        
        # Auto-detect target columns (disease columns)
        self.target_cols = []
        for col in df.columns:
            if any(keyword in col.lower() for keyword in disease_keywords):
                if df[col].dtype in ['int64', 'float64'] and df[col].nunique() <= 10:
                    self.target_cols.append(col)
        
        # If no disease columns found, assume last few columns are targets
        if not self.target_cols:
            self.target_cols = df.columns[-5:].tolist()
        
        # Feature columns are everything else (numeric only)
        self.feature_cols = [col for col in df.columns 
                           if col not in self.target_cols and 
                           df[col].dtype in ['int64', 'float64']]
        
        print(f"🎯 Auto-detected {len(self.feature_cols)} features, {len(self.target_cols)} targets")
        print(f"Features: {self.feature_cols[:5]}...")
        print(f"Targets: {self.target_cols}")
        
    def preprocess_data(self, df):
        """Ultra-fast preprocessing"""
        # Fill missing values with mean
        df = df.fillna(df.mean(numeric_only=True))
        
        # Convert categorical to numeric
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = pd.Categorical(df[col]).codes
        
        return df
    
    def train_ultra_fast(self, csv_path):
        """Train model in under 30 seconds"""
        print("⚡ Loading data...")
        df = pd.read_csv(csv_path)
        
        # Auto-detect columns
        self.auto_detect_columns(df)
        
        # Preprocess
        df = self.preprocess_data(df)
        
        # Prepare data
        X = df[self.feature_cols]
        y = df[self.target_cols]
        
        # Convert targets to binary if needed
        for col in self.target_cols:
            if y[col].nunique() > 2:
                y[col] = (y[col] > y[col].median()).astype(int)
        
        print(f"📊 Data shape: {X.shape}, Targets: {y.shape}")
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train XGBoost (fastest and most accurate)
        print("🚀 Training XGBoost...")
        self.model = MultiOutputClassifier(
            xgb.XGBClassifier(
                n_estimators=50,  # Reduced for speed
                max_depth=6,
                random_state=42,
                n_jobs=-1  # Use all cores
            )
        )
        
        self.model.fit(X_train_scaled, y_train)
        
        # Quick evaluation
        y_pred = self.model.predict(X_test_scaled)
        accuracy = accuracy_score(y_test, y_pred)
        
        print(f"🎯 Model Accuracy: {accuracy:.3f}")
        
        # Save model
        os.makedirs('models', exist_ok=True)
        joblib.dump(self.model, 'models/predictor.pkl')
        joblib.dump(self.scaler, 'models/scaler.pkl')
        joblib.dump({'features': self.feature_cols, 'targets': self.target_cols}, 
                   'models/columns.pkl')
        
        return accuracy
    
    def predict_diseases(self, input_data):
        """Make predictions"""
        if self.model is None:
            self.load_model()
        
        # Convert to numpy array
        if isinstance(input_data, dict):
            input_data = [input_data[col] for col in self.feature_cols]
        
        # Scale and predict
        input_scaled = self.scaler.transform([input_data])
        predictions = self.model.predict(input_scaled)[0]
        probabilities = self.model.predict_proba(input_scaled)
        
        # Format results
        results = []
        for i, disease in enumerate(self.target_cols):
            prob = np.max([p[i] for p in probabilities if len(p) > i])
            results.append({
                'disease': disease,
                'risk': 'HIGH' if predictions[i] == 1 else 'LOW',
                'confidence': f"{prob*100:.1f}%"
            })
        
        return results
    
    def load_model(self):
        """Load saved model"""
        self.model = joblib.load('models/predictor.pkl')
        self.scaler = joblib.load('models/scaler.pkl')
        cols = joblib.load('models/columns.pkl')
        self.feature_cols = cols['features']
        self.target_cols = cols['targets']