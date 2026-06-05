# 🎨 Anime AI Image Generator

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![Replicate](https://img.shields.io/badge/AI-Replicate-orange.svg)](https://replicate.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Overview

A **production-ready Anime AI Image Generator** with a beautiful frontend interface and robust backend API. This full-stack application demonstrates:

- 🎨 AI-powered image generation from text prompts
- 🌐 RESTful API design with Flask
- 💎 Modern, responsive UI/UX
- 🔌 Modular architecture supporting multiple AI providers
- 🛡️ Graceful fallback system for API rate limiting

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Text-to-Image Generation** | Convert text prompts to anime-style artwork |
| **HD Resolution** | Support for 512x512, 768x768, and 1024x1024 images |
| **Download Capability** | Save generated images to your device |
| **Responsive UI** | Works on desktop, tablet, and mobile |
| **Real-time Feedback** | Loading states and error handling |
| **API Ready** | REST endpoints for programmatic access |

## 🏗️ Architecture

User Browser (Frontend)
↓
Flask Backend
↓
┌─────┼─────┐
↓ ↓ ↓
Replicate Hugging Face Fallback
API API Generator


## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | HTML5, CSS3, JavaScript |
| **Backend** | Python, Flask |
| **AI Providers** | Replicate API, Hugging Face Inference |
| **Image Processing** | Pillow |
| **Container** | Docker |

## 📦 Installation

### Local Development

```bash
# Clone repository
git clone https://github.com/Aikaksh-Singh-Routela/anime-ai-generator.git
cd anime-ai-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Set API key (optional - app works in demo mode without it)
export REPLICATE_API_TOKEN="your-token-here"

# Run the backend
python app.py

# Open frontend in browser
open frontend/index.html

docker build -t anime-ai-generator .
docker run -p 5000:5000 -e REPLICATE_API_TOKEN="your-token" anime-ai-generator

curl -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "beautiful anime girl with pink hair, cyberpunk city"}'

