from flask import Flask, render_template_string, request, jsonify
from predictor import UltraPredictor
import os

app = Flask(__name__)
predictor = UltraPredictor()

# Load model if exists
if os.path.exists('models/predictor.pkl'):
    predictor.load_model()

# Ultra-minimal HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>⚡ Disease Predictor</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh; padding: 20px;
        }
        .container { 
            max-width: 800px; margin: 0 auto; 
            background: white; border-radius: 20px; 
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        .header { 
            background: linear-gradient(135deg, #ff6b6b, #4ecdc4);
            color: white; padding: 30px; text-align: center;
        }
        .header h1 { font-size: 2.5rem; margin-bottom: 10px; }
        .form-container { padding: 30px; }
        .form-group { margin-bottom: 20px; }
        label { display: block; margin-bottom: 5px; font-weight: 600; color: #333; }
        input, select { 
            width: 100%; padding: 12px; border: 2px solid #ddd; 
            border-radius: 8px; font-size: 16px; transition: border-color 0.3s;
        }
        input:focus, select:focus { 
            outline: none; border-color: #667eea; 
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        .btn { 
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white; padding: 15px 30px; border: none; 
            border-radius: 8px; font-size: 18px; cursor: pointer;
            width: 100%; transition: transform 0.3s;
        }
        .btn:hover { transform: translateY(-2px); }
        .results { 
            margin-top: 30px; padding: 20px; 
            background: #f8f9fa; border-radius: 10px;
        }
        .disease-card { 
            background: white; padding: 15px; margin: 10px 0; 
            border-radius: 8px; border-left: 4px solid #667eea;
            display: flex; justify-content: space-between; align-items: center;
        }
        .risk-high { border-left-color: #ff6b6b; }
        .risk-low { border-left-color: #4ecdc4; }
        .risk-badge { 
            padding: 5px 15px; border-radius: 20px; font-weight: 600;
            font-size: 14px;
        }
        .risk-high .risk-badge { background: #ff6b6b; color: white; }
        .risk-low .risk-badge { background: #4ecdc4; color: white; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }
        @media (max-width: 768px) { 
            .header h1 { font-size: 2rem; }
            .form-container { padding: 20px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>⚡ AI Disease Predictor</h1>
            <p>Ultra-fast multi-disease risk assessment</p>
        </div>
        
        <div class="form-container">
            <form id="predictionForm">
                <div class="grid">
                    {% for feature in features %}
                    <div class="form-group">
                        <label>{{ feature.replace('_', ' ').title() }}</label>
                        <input type="number" name="{{ feature }}" step="0.01" required>
                    </div>
                    {% endfor %}
                </div>
                <button type="submit" class="btn">🔍 Predict Disease Risk</button>
            </form>
            
            <div id="results" class="results" style="display: none;">
                <h3>📊 Risk Assessment Results</h3>
                <div id="disease-results"></div>
            </div>
        </div>
    </div>
    
    <script>
        document.getElementById('predictionForm').onsubmit = async (e) => {
            e.preventDefault();
            
            const formData = new FormData(e.target);
            const data = Object.fromEntries(formData);
            
            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                
                const results = await response.json();
                
                let html = '';
                results.forEach(result => {
                    const riskClass = result.risk === 'HIGH' ? 'risk-high' : 'risk-low';
                    html += `
                        <div class="disease-card ${riskClass}">
                            <div>
                                <strong>${result.disease.replace('_', ' ').toUpperCase()}</strong>
                                <div style="color: #666; font-size: 14px;">Confidence: ${result.confidence}</div>
                            </div>
                            <div class="risk-badge">${result.risk} RISK</div>
                        </div>
                    `;
                });
                
                document.getElementById('disease-results').innerHTML = html;
                document.getElementById('results').style.display = 'block';
                
            } catch (error) {
                alert('Error making prediction: ' + error.message);
            }
        };
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, features=predictor.feature_cols)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = [float(data.get(col, 0)) for col in predictor.feature_cols]
        results = predictor.predict_diseases(features)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)