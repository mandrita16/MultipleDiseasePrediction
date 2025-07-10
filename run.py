#!/usr/bin/env python3
"""
🚀 Ultra-Fast Disease Predictor
One command to rule them all!
"""

import os
import sys
from predictor import UltraPredictor

def main():
    print("⚡ ULTRA-FAST DISEASE PREDICTOR STARTING...")
    
    # Check for dataset
    dataset_path = 'data/disease_dataset.csv'
    if not os.path.exists(dataset_path):
        print(f"❌ Dataset not found at {dataset_path}")
        print("📁 Place your CSV file in the data/ directory")
        return
    
    # Initialize predictor
    predictor = UltraPredictor()
    
    # Train model if not exists
    if not os.path.exists('models/predictor.pkl'):
        print("🤖 Training model...")
        accuracy = predictor.train_ultra_fast(dataset_path)
        print(f"✅ Model trained! Accuracy: {accuracy:.3f}")
    else:
        print("✅ Model already exists, loading...")
        predictor.load_model()
    
    # Start web app
    print("🌐 Starting web interface...")
    print("🚀 Open your browser and go to: http://localhost:5000")
    print("🎯 Ready to predict diseases!")
    
    from app import app
    app.run(debug=False, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()