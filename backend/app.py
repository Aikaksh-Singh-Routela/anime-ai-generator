# app.py - Anime AI Generator with Replicate API
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import requests
import replicate
import os

app = Flask(__name__)
CORS(app)

# Get token from environment variable
REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN", "")

print(f"Token loaded: {'Yes' if REPLICATE_API_TOKEN else 'No'}")

# Model for anime generation
MODEL = "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b"

def generate_with_replicate(prompt):
    """Generate REAL AI image using Replicate"""
    if not REPLICATE_API_TOKEN:
        print("No API token found!")
        return None
    
    try:
        print(f"🎨 Calling Replicate API...")
        
        output = replicate.run(
            MODEL,
            input={
                "prompt": f"anime style, masterpiece, best quality, {prompt}",
                "negative_prompt": "low quality, blurry, distorted, ugly",
                "width": 512,
                "height": 512,
                "num_outputs": 1,
                "num_inference_steps": 25,
                "guidance_scale": 7.5
            }
        )
        
        if output and len(output) > 0:
            image_url = output[0]
            response = requests.get(image_url, timeout=30)
            if response.status_code == 200:
                return base64.b64encode(response.content).decode('utf-8')
        return None
    except Exception as e:
        print(f"Replicate error: {e}")
        return None

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'token_configured': bool(REPLICATE_API_TOKEN)})

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    
    if not prompt:
        return jsonify({'error': 'No prompt'}), 400
    
    print(f"🎨 Generating for: {prompt[:50]}...")
    
    image_base64 = generate_with_replicate(prompt)
    
    if image_base64:
        return jsonify({
            'success': True,
            'image': image_base64,
            'prompt': prompt,
            'source': 'Replicate AI'
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Replicate API failed. Check token or try again.'
        }), 503

if __name__ == '__main__':
    print("🎨 Anime AI Generator with Replicate")
    print(f"Token configured: {'Yes' if REPLICATE_API_TOKEN else 'No'}")
    app.run(host='0.0.0.0', port=5000, debug=True)